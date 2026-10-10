# ====================================================================
# BHAKTI APP: REST API CONTROLLER
# Connects HTTP Requests to Database Engine with JSON Responses
# ====================================================================

import json
import urllib.parse
from typing import Dict, Any, Tuple
from db.database import BhaktiDB
from core.validator import validate_content_data
from bulk_import.importer import run_bulk_import

db = BhaktiDB()

def handle_api_request(method: str, path: str, query_params: Dict[str, str], body_data: Any) -> Tuple[int, str, bytes]:
    """
    Dispatches API requests and returns (status_code, content_type, response_bytes).
    """
    headers_ct = "application/json; charset=utf-8"

    try:
        # 1. GET /api/masters (Deities, Content Types, Categories)
        if method == "GET" and path == "/api/masters":
            conn = db.get_connection()
            cur = conn.cursor()
            cur.execute("SELECT * FROM deities WHERE is_active = 1 ORDER BY display_order")
            deities = [dict(r) for r in cur.fetchall()]
            cur.execute("SELECT * FROM content_types WHERE is_active = 1 ORDER BY display_order")
            content_types = [dict(r) for r in cur.fetchall()]
            cur.execute("SELECT * FROM categories ORDER BY display_order")
            categories = [dict(r) for r in cur.fetchall()]
            conn.close()
            return (200, headers_ct, json.dumps({'deities': deities, 'content_types': content_types, 'categories': categories}, ensure_ascii=False).encode('utf-8'))

        # 2. GET /api/stats (Admin Analytics)
        if method == "GET" and path == "/api/stats":
            stats = db.get_stats()
            return (200, headers_ct, json.dumps(stats, ensure_ascii=False).encode('utf-8'))

        # 3. GET /api/content (Paginated List)
        if method == "GET" and path == "/api/content":
            ctype = query_params.get('type') or query_params.get('content_type')
            if ctype in ('all', '', 'null', 'undefined'):
                ctype = None
            deity = query_params.get('deity') or query_params.get('deity_id')
            if deity in ('all', '', 'null', 'undefined'):
                deity = None
            cat = query_params.get('category') or query_params.get('category_id')
            if cat in ('all', '', 'null', 'undefined'):
                cat = None
            status = query_params.get('status', 'published')
            
            is_pop = True if query_params.get('popular') == '1' else None
            is_feat = True if query_params.get('featured') == '1' else None
            is_trend = True if query_params.get('trending') == '1' else None
            
            limit = min(100, int(query_params.get('limit', 20)))
            page = max(1, int(query_params.get('page', 1)))

            has_audio = True if query_params.get('has_audio') == '1' else None
            audio_source = query_params.get('audio_source') or query_params.get('source')
            if audio_source in ('all', '', 'null', 'undefined'):
                audio_source = None

            # If search query provided
            q = query_params.get('q') or query_params.get('search')
            if q:
                res = db.search_content(query=q, content_type=ctype, deity_id=deity, status=status, has_audio=has_audio, audio_source=audio_source, limit=limit, page=page)
            else:
                res = db.get_content_paginated(
                    content_type=ctype,
                    deity_id=deity,
                    category_id=cat,
                    status=status,
                    is_popular=is_pop,
                    is_featured=is_feat,
                    is_trending=is_trend,
                    has_audio=has_audio,
                    audio_source=audio_source,
                    limit=limit,
                    page=page
                )
            return (200, headers_ct, json.dumps(res, ensure_ascii=False).encode('utf-8'))

        # 3.5 GET /api/audio-library (Dedicated Audio Collection)
        if method == "GET" and path == "/api/audio-library":
            q = query_params.get('q') or query_params.get('search')
            ctype = query_params.get('type')
            if ctype in ('all', '', 'null', 'undefined'): ctype = None
            source = query_params.get('source') or query_params.get('audio_source')
            if source in ('all', '', 'null', 'undefined'): source = None
            deity = query_params.get('deity')
            if deity in ('all', '', 'null', 'undefined'): deity = None
            limit = min(200, int(query_params.get('limit', 100)))
            page = max(1, int(query_params.get('page', 1)))

            status = query_params.get('status')
            if status in ('all', '', 'null', 'undefined'): status = None

            if q:
                res = db.search_content(query=q, content_type=ctype, deity_id=deity, has_audio=True, audio_source=source, status=status, limit=limit, page=page)
            else:
                res = db.get_content_paginated(content_type=ctype, deity_id=deity, has_audio=True, audio_source=source, status=status, limit=limit, page=page)

            # Query Audio Statistics
            conn = db.get_connection()
            cur = conn.cursor()
            cur.execute("SELECT COUNT(*) FROM content_items WHERE (audio_url LIKE 'assets/audio/%' OR audio_url LIKE 'https://www.youtube.com/%' OR audio_url LIKE 'https://youtu.be/%')")
            total_audio = cur.fetchone()[0]
            cur.execute("SELECT COUNT(*) FROM content_items WHERE audio_url LIKE 'assets/audio/%'")
            local_cnt = cur.fetchone()[0]
            cur.execute("SELECT COUNT(*) FROM content_items WHERE audio_url LIKE 'https://www.youtube.com/%' OR audio_url LIKE 'https://youtu.be/%'")
            yt_cnt = cur.fetchone()[0]
            conn.close()

            res['audio_stats'] = {
                'total_playable': total_audio,
                'local_mp3': local_cnt,
                'youtube_hd': yt_cnt
            }
            return (200, headers_ct, json.dumps(res, ensure_ascii=False).encode('utf-8'))

        # 4. GET /api/content/<id>
        if method == "GET" and path.startswith("/api/content/"):
            item_id = path.replace("/api/content/", "").strip()
            item = db.get_content_by_id(item_id)
            if not item:
                return (404, headers_ct, json.dumps({'error': 'Item not found'}, ensure_ascii=False).encode('utf-8'))
            return (200, headers_ct, json.dumps(item, ensure_ascii=False).encode('utf-8'))

        # 5. POST /api/admin/content (Create Item)
        if method == "POST" and path == "/api/admin/content":
            if not body_data:
                return (400, headers_ct, json.dumps({'error': 'Missing JSON body'}).encode('utf-8'))
            
            is_valid, errors = validate_content_data(body_data)
            if not is_valid:
                return (422, headers_ct, json.dumps({'error': 'Validation failed', 'details': errors}, ensure_ascii=False).encode('utf-8'))

            success, msg, item_id = db.insert_content(body_data, on_duplicate=query_params.get('on_duplicate', 'skip'))
            status_code = 201 if success else 409
            return (status_code, headers_ct, json.dumps({'success': success, 'message': msg, 'id': item_id}, ensure_ascii=False).encode('utf-8'))

        # 6. PUT /api/admin/content/<id> (Update Item)
        if method == "PUT" and path.startswith("/api/admin/content/"):
            item_id = path.replace("/api/admin/content/", "").strip()
            if not body_data:
                return (400, headers_ct, json.dumps({'error': 'Missing JSON body'}).encode('utf-8'))
            
            body_data['id'] = item_id
            success, msg, _ = db.insert_content(body_data, on_duplicate='overwrite')
            return (200, headers_ct, json.dumps({'success': success, 'message': msg, 'id': item_id}, ensure_ascii=False).encode('utf-8'))

        # 7. PATCH /api/admin/content/<id>/status
        if method == "PATCH" and path.startswith("/api/admin/content/") and path.endswith("/status"):
            item_id = path.split("/")[4]
            new_status = body_data.get('status') if isinstance(body_data, dict) else query_params.get('status')
            if not new_status:
                return (400, headers_ct, json.dumps({'error': 'Missing new status'}).encode('utf-8'))
            
            ok = db.update_status(item_id, new_status)
            return (200 if ok else 404, headers_ct, json.dumps({'success': ok, 'id': item_id, 'status': new_status}).encode('utf-8'))

        # 8. DELETE /api/admin/content/<id>
        if method == "DELETE" and path.startswith("/api/admin/content/"):
            item_id = path.replace("/api/admin/content/", "").strip()
            ok = db.delete_content(item_id)
            return (200 if ok else 404, headers_ct, json.dumps({'success': ok, 'id': item_id}).encode('utf-8'))

        # 9. POST /api/admin/bulk-import (JSON Payload)
        if method == "POST" and path == "/api/admin/bulk-import":
            if not body_data:
                return (400, headers_ct, json.dumps({'error': 'Missing payload'}).encode('utf-8'))
            
            items = body_data if isinstance(body_data, list) else body_data.get('items', [])
            on_dup = query_params.get('on_duplicate', 'skip')
            dry_run = query_params.get('dry_run') in ('1', 'true', 'yes')

            if dry_run:
                valid_count = 0
                val_errors = []
                for idx, it in enumerate(items):
                    v, errs = validate_content_data(it)
                    if v: valid_count += 1
                    else: val_errors.append(f"Item {idx+1}: {', '.join(errs)}")
                return (200, headers_ct, json.dumps({
                    'dry_run': True,
                    'total': len(items),
                    'valid': valid_count,
                    'invalid': len(val_errors),
                    'errors': val_errors[:20]
                }, ensure_ascii=False).encode('utf-8'))

            res = db.bulk_insert(items, on_duplicate=on_dup)
            return (200, headers_ct, json.dumps(res, ensure_ascii=False).encode('utf-8'))

        return (404, headers_ct, json.dumps({'error': 'Not Found'}).encode('utf-8'))

    except Exception as e:
        return (500, headers_ct, json.dumps({'error': str(e)}).encode('utf-8'))
