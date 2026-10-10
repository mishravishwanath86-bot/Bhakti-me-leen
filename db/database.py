# ====================================================================
# BHAKTI APP: SQLITE DATABASE MANAGER WITH FTS5 & BULK TRANSACTIONS
# ====================================================================

import os
import sqlite3
import json
from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime, timezone

from core.models import ContentItem
from core.normalizer import build_search_tokens, build_fts_query
from core.deduplicator import generate_content_hash, generate_slug

DB_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_DB_PATH = os.path.join(DB_DIR, "bhakti.db")
SCHEMA_PATH = os.path.join(DB_DIR, "schema.sql")
SEED_PATH = os.path.join(DB_DIR, "seed_masters.sql")

class BhaktiDB:
    def __init__(self, db_path: str = DEFAULT_DB_PATH):
        self.db_path = db_path
        self._init_db()

    def get_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON;")
        conn.execute("PRAGMA journal_mode = WAL;")
        conn.execute("PRAGMA synchronous = NORMAL;")
        return conn

    def _init_db(self):
        """Creates tables, indexes, FTS5 virtual tables and master seeds if not exist."""
        conn = self.get_connection()
        try:
            with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
                conn.executescript(f.read())
            with open(SEED_PATH, "r", encoding="utf-8") as f:
                conn.executescript(f.read())
            conn.commit()
        finally:
            conn.close()

    def insert_content(self, data: Dict[str, Any], on_duplicate: str = 'skip') -> Tuple[bool, str, Optional[str]]:
        """
        Inserts a single ContentItem.
        on_duplicate: 'skip' | 'overwrite' | 'error'
        Returns (success, message, item_id)
        """
        conn = self.get_connection()
        try:
            title = data['title'].strip()
            deity_id = data['deity_id'].strip().lower()
            content_type = data['content_type'].strip().lower()
            
            content_hash = data.get('content_hash') or generate_content_hash(title, deity_id, content_type)
            item_id = data.get('id') or generate_slug(content_type, deity_id, title)
            
            # Check duplicate by hash
            cur = conn.cursor()
            cur.execute("SELECT id, title FROM content_items WHERE content_hash = ?", (content_hash,))
            existing = cur.fetchone()
            
            if existing:
                if on_duplicate == 'skip':
                    return (False, f"Skipped: Duplicate of '{existing['title']}' (ID: {existing['id']})", existing['id'])
                elif on_duplicate == 'error':
                    raise ValueError(f"Duplicate content detected: '{existing['title']}' (ID: {existing['id']})")
                elif on_duplicate == 'overwrite':
                    item_id = existing['id']

            # Build search tokens
            tags = data.get('tags', [])
            if isinstance(tags, str):
                try: tags = json.loads(tags)
                except: tags = [t.strip() for t in tags.split(',') if t.strip()]

            search_keywords = build_search_tokens(
                title=title,
                title_en=data.get('title_en'),
                deity_id=deity_id,
                content_type=content_type,
                tags=tags,
                short_desc=data.get('short_description')
            )

            now_iso = datetime.now(timezone.utc).isoformat()
            
            item = ContentItem(
                id=item_id,
                title=title,
                title_en=data.get('title_en'),
                deity_id=deity_id,
                category_id=data.get('category_id', 'bhakti'),
                content_type=content_type,
                language=data.get('language', 'hi'),
                short_description=data.get('short_description'),
                content=data['content'],
                thumbnail=data.get('thumbnail'),
                audio_url=data.get('audio_url'),
                video_url=data.get('video_url'),
                duration=int(data.get('duration', 0)),
                tags=tags,
                is_popular=bool(data.get('is_popular', False)),
                is_featured=bool(data.get('is_featured', False)),
                is_trending=bool(data.get('is_trending', False)),
                status=data.get('status', 'published'),
                content_hash=content_hash,
                search_keywords=search_keywords,
                created_at=data.get('created_at', now_iso),
                updated_at=now_iso
            )

            row = item.to_db_row()
            columns = list(row.keys())
            placeholders = [":" + k for k in columns]

            sql = f"""
                INSERT OR REPLACE INTO content_items ({', '.join(columns)})
                VALUES ({', '.join(placeholders)})
            """
            cur.execute(sql, row)
            conn.commit()
            return (True, "Content saved successfully", item_id)
        finally:
            conn.close()

    def get_content_paginated(
        self,
        content_type: Optional[str] = None,
        deity_id: Optional[str] = None,
        category_id: Optional[str] = None,
        status: str = 'published',
        is_popular: Optional[bool] = None,
        is_featured: Optional[bool] = None,
        is_trending: Optional[bool] = None,
        has_audio: Optional[bool] = None,
        audio_source: Optional[str] = None,
        limit: int = 20,
        page: int = 1,
        cursor: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        High-performance indexed pagination. Supports offset and cursor pagination.
        """
        conn = self.get_connection()
        try:
            cur = conn.cursor()
            conditions = []
            params: List[Any] = []

            if status:
                conditions.append("c.status = ?")
                params.append(status)

            if content_type:
                conditions.append("c.content_type = ?")
                params.append(content_type)

            if deity_id:
                conditions.append("c.deity_id = ?")
                params.append(deity_id)

            if category_id:
                conditions.append("c.category_id = ?")
                params.append(category_id)

            if is_popular is not None:
                conditions.append("c.is_popular = ?")
                params.append(1 if is_popular else 0)

            if is_featured is not None:
                conditions.append("c.is_featured = ?")
                params.append(1 if is_featured else 0)

            if is_trending is not None:
                conditions.append("c.is_trending = ?")
                params.append(1 if is_trending else 0)

            if has_audio:
                if audio_source == 'local':
                    conditions.append("c.audio_url LIKE 'assets/audio/%'")
                elif audio_source == 'youtube':
                    conditions.append("(c.audio_url LIKE 'https://www.youtube.com/%' OR c.audio_url LIKE 'https://youtu.be/%')")
                else:
                    conditions.append("(c.audio_url LIKE 'assets/audio/%' OR c.audio_url LIKE 'https://www.youtube.com/%' OR c.audio_url LIKE 'https://youtu.be/%')")

            where_clause = " AND ".join(conditions) if conditions else "1=1"

            # Count total
            count_sql = f"SELECT COUNT(*) FROM content_items c WHERE {where_clause}"
            cur.execute(count_sql, params)
            total_items = cur.fetchone()[0]

            # Query items
            offset = max(0, (page - 1) * limit)
            query_sql = f"""
                SELECT c.*, d.name_hi as deity_name_hi, ct.name_hi as type_name_hi
                FROM content_items c
                LEFT JOIN deities d ON c.deity_id = d.id
                LEFT JOIN content_types ct ON c.content_type = ct.id
                WHERE {where_clause}
                ORDER BY c.created_at DESC, c.id DESC
                LIMIT ? OFFSET ?
            """
            cur.execute(query_sql, params + [limit, offset])
            rows = [dict(r) for r in cur.fetchall()]

            # Decode tags JSON
            for r in rows:
                if 'tags' in r and isinstance(r['tags'], str):
                    try: r['tags'] = json.loads(r['tags'])
                    except: r['tags'] = []

            total_pages = (total_items + limit - 1) // limit if total_items > 0 else 1

            return {
                'items': rows,
                'pagination': {
                    'total_items': total_items,
                    'page': page,
                    'limit': limit,
                    'total_pages': total_pages,
                    'has_next': page < total_pages,
                    'has_prev': page > 1
                }
            }
        finally:
            conn.close()

    def search_content(
        self,
        query: str,
        content_type: Optional[str] = None,
        deity_id: Optional[str] = None,
        status: Optional[str] = None,
        has_audio: Optional[bool] = None,
        audio_source: Optional[str] = None,
        limit: int = 20,
        page: int = 1
    ) -> Dict[str, Any]:
        """
        Full-Text Search using SQLite FTS5 with BM25 relevance ranking.
        """
        if not query or not query.strip():
            return self.get_content_paginated(content_type=content_type, deity_id=deity_id, status=status, has_audio=has_audio, audio_source=audio_source, limit=limit, page=page)

        fts_query = build_fts_query(query)
        if not fts_query:
            return {'items': [], 'pagination': {'total_items': 0, 'page': page, 'limit': limit, 'total_pages': 0}}

        conn = self.get_connection()
        try:
            cur = conn.cursor()
            conditions = []
            params: List[Any] = []

            if status:
                conditions.append("c.status = ?")
                params.append(status)

            if content_type:
                conditions.append("c.content_type = ?")
                params.append(content_type)

            if deity_id:
                conditions.append("c.deity_id = ?")
                params.append(deity_id)

            if has_audio:
                if audio_source == 'local':
                    conditions.append("c.audio_url LIKE 'assets/audio/%'")
                elif audio_source == 'youtube':
                    conditions.append("(c.audio_url LIKE 'https://www.youtube.com/%' OR c.audio_url LIKE 'https://youtu.be/%')")
                else:
                    conditions.append("(c.audio_url LIKE 'assets/audio/%' OR c.audio_url LIKE 'https://www.youtube.com/%' OR c.audio_url LIKE 'https://youtu.be/%')")

            where_clause = " AND ".join(conditions) if conditions else "1=1"

            # Count matches
            count_sql = f"""
                SELECT COUNT(*)
                FROM content_fts f
                JOIN content_items c ON f.content_id = c.id
                WHERE content_fts MATCH ? AND {where_clause}
            """
            cur.execute(count_sql, [fts_query] + params)
            total_items = cur.fetchone()[0]

            offset = max(0, (page - 1) * limit)
            search_sql = f"""
                SELECT c.*, d.name_hi as deity_name_hi, ct.name_hi as type_name_hi,
                       bm25(content_fts) as rank
                FROM content_fts f
                JOIN content_items c ON f.content_id = c.id
                LEFT JOIN deities d ON c.deity_id = d.id
                LEFT JOIN content_types ct ON c.content_type = ct.id
                WHERE content_fts MATCH ? AND {where_clause}
                ORDER BY rank
                LIMIT ? OFFSET ?
            """
            cur.execute(search_sql, [fts_query] + params + [limit, offset])
            rows = [dict(r) for r in cur.fetchall()]

            for r in rows:
                if 'tags' in r and isinstance(r['tags'], str):
                    try: r['tags'] = json.loads(r['tags'])
                    except: r['tags'] = []

            total_pages = (total_items + limit - 1) // limit if total_items > 0 else 1

            return {
                'query': query,
                'items': rows,
                'pagination': {
                    'total_items': total_items,
                    'page': page,
                    'limit': limit,
                    'total_pages': total_pages,
                    'has_next': page < total_pages
                }
            }
        finally:
            conn.close()

    def get_content_by_id(self, item_id: str) -> Optional[Dict[str, Any]]:
        conn = self.get_connection()
        try:
            cur = conn.cursor()
            cur.execute("""
                SELECT c.*, d.name_hi as deity_name_hi, ct.name_hi as type_name_hi
                FROM content_items c
                LEFT JOIN deities d ON c.deity_id = d.id
                LEFT JOIN content_types ct ON c.content_type = ct.id
                WHERE c.id = ?
            """, (item_id,))
            row = cur.fetchone()
            if not row:
                return None
            res = dict(row)
            if 'tags' in res and isinstance(res['tags'], str):
                try: res['tags'] = json.loads(res['tags'])
                except: res['tags'] = []
            return res
        finally:
            conn.close()

    def update_status(self, item_id: str, new_status: str) -> bool:
        if new_status not in ('draft', 'published', 'archived'):
            raise ValueError(f"Invalid status: {new_status}")
        conn = self.get_connection()
        try:
            cur = conn.cursor()
            now_iso = datetime.now(timezone.utc).isoformat()
            cur.execute("UPDATE content_items SET status = ?, updated_at = ? WHERE id = ?", (new_status, now_iso, item_id))
            conn.commit()
            return cur.rowcount > 0
        finally:
            conn.close()

    def delete_content(self, item_id: str) -> bool:
        conn = self.get_connection()
        try:
            cur = conn.cursor()
            cur.execute("DELETE FROM content_items WHERE id = ?", (item_id,))
            conn.commit()
            return cur.rowcount > 0
        finally:
            conn.close()

    def get_stats(self) -> Dict[str, Any]:
        """Returns comprehensive statistics for the admin dashboard."""
        conn = self.get_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT COUNT(*) FROM content_items")
            total = cur.fetchone()[0]

            cur.execute("SELECT status, COUNT(*) FROM content_items GROUP BY status")
            by_status = {r[0]: r[1] for r in cur.fetchall()}

            cur.execute("SELECT content_type, COUNT(*) FROM content_items GROUP BY content_type")
            by_type = {r[0]: r[1] for r in cur.fetchall()}

            cur.execute("SELECT deity_id, COUNT(*) FROM content_items GROUP BY deity_id")
            by_deity = {r[0]: r[1] for r in cur.fetchall()}

            return {
                'total_items': total,
                'by_status': by_status,
                'by_type': by_type,
                'by_deity': by_deity
            }
        finally:
            conn.close()

    def bulk_insert(self, items: List[Dict[str, Any]], on_duplicate: str = 'skip') -> Dict[str, Any]:
        """
        Blazing-fast chunked transaction import for 5,000 to 50,000+ items.
        """
        conn = self.get_connection()
        added_count = 0
        skipped_count = 0
        overwritten_count = 0
        error_details = []

        try:
            # Pre-load existing hashes for O(1) in-memory check
            cur = conn.cursor()
            cur.execute("SELECT content_hash, id FROM content_items")
            existing_hashes = {r[0]: r[1] for r in cur.fetchall()}

            rows_to_insert = []
            now_iso = datetime.now(timezone.utc).isoformat()

            for idx, raw in enumerate(items):
                try:
                    title = raw.get('title', '').strip()
                    deity_id = raw.get('deity_id', '').strip().lower()
                    content_type = raw.get('content_type', '').strip().lower()

                    if not title or not deity_id or not content_type:
                        error_details.append(f"Row {idx+1}: Missing title, deity_id, or content_type")
                        continue

                    chash = raw.get('content_hash') or generate_content_hash(title, deity_id, content_type)
                    item_id = raw.get('id') or generate_slug(content_type, deity_id, title)

                    if chash in existing_hashes:
                        if on_duplicate == 'skip':
                            skipped_count += 1
                            continue
                        elif on_duplicate == 'overwrite':
                            item_id = existing_hashes[chash]
                            overwritten_count += 1
                        elif on_duplicate == 'error':
                            raise ValueError(f"Duplicate at row {idx+1}: '{title}'")

                    tags = raw.get('tags', [])
                    if isinstance(tags, str):
                        try: tags = json.loads(tags)
                        except: tags = [t.strip() for t in tags.split(',') if t.strip()]

                    search_keywords = build_search_tokens(
                        title=title,
                        title_en=raw.get('title_en'),
                        deity_id=deity_id,
                        content_type=content_type,
                        tags=tags,
                        short_desc=raw.get('short_description')
                    )

                    item = ContentItem(
                        id=item_id,
                        title=title,
                        title_en=raw.get('title_en'),
                        deity_id=deity_id,
                        category_id=raw.get('category_id', 'bhakti'),
                        content_type=content_type,
                        language=raw.get('language', 'hi'),
                        short_description=raw.get('short_description'),
                        content=raw.get('content', ''),
                        thumbnail=raw.get('thumbnail'),
                        audio_url=raw.get('audio_url'),
                        video_url=raw.get('video_url'),
                        duration=int(raw.get('duration', 0)),
                        tags=tags,
                        is_popular=bool(raw.get('is_popular', False)),
                        is_featured=bool(raw.get('is_featured', False)),
                        is_trending=bool(raw.get('is_trending', False)),
                        status=raw.get('status', 'published'),
                        content_hash=chash,
                        search_keywords=search_keywords,
                        created_at=raw.get('created_at', now_iso),
                        updated_at=now_iso
                    )

                    rows_to_insert.append(item.to_db_row())
                    existing_hashes[chash] = item_id

                except Exception as e:
                    error_details.append(f"Row {idx+1} error: {str(e)}")

            # Batch insert in chunks of 500
            chunk_size = 500
            for i in range(0, len(rows_to_insert), chunk_size):
                chunk = rows_to_insert[i:i+chunk_size]
                if not chunk: continue
                columns = list(chunk[0].keys())
                placeholders = [":" + k for k in columns]
                sql = f"INSERT OR REPLACE INTO content_items ({', '.join(columns)}) VALUES ({', '.join(placeholders)})"
                cur.executemany(sql, chunk)
                conn.commit()
                added_count += len(chunk)

            return {
                'success': True,
                'total_processed': len(items),
                'added': added_count,
                'skipped_duplicates': skipped_count,
                'overwritten': overwritten_count,
                'errors_count': len(error_details),
                'error_details': error_details[:50]
            }
        finally:
            conn.close()
