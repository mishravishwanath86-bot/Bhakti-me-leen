import sqlite3
import json
import hashlib
import sys
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

DB_PATH = 'db/bhakti.db'
JSON_PATH = 'drik_sundarkand_dohas.json'

def main():
    print("1. Connecting to DB...")
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Ensure sundarkand is in content_types
    cur.execute("SELECT id FROM content_types WHERE id = 'sundarkand'")
    if not cur.fetchone():
        print("Registering 'sundarkand' in content_types...")
        cur.execute("""
            INSERT INTO content_types (id, name_hi, name_en, icon, display_order, is_active)
            VALUES ('sundarkand', 'सुंदरकांड', 'Sundarkand', 'scroll', 14, 1)
        """)
        conn.commit()
        print("✓ Registered 'sundarkand' in content_types")
    else:
        print("✓ 'sundarkand' already present in content_types")

    # Load JSON
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    dohas = data.get('dohas', [])
    print(f"Loaded {len(dohas)} dohas from {JSON_PATH}")

    now = datetime.now().isoformat()
    inserted_count = 0
    updated_count = 0

    for d in dohas:
        doha_num = d['doha_number']
        item_id = f"sundarkand-doha-{doha_num}"
        title_hi = f"सुन्दरकाण्ड दोहा {doha_num}: {d['title']}"
        title_en = f"Sundarkand Doha {doha_num}"
        
        # Build complete scripture content preserving all lines
        content_parts = []
        if d.get('shloka') and len(d['shloka']) > 0:
            content_parts.append("॥ मंगलाचरण श्लोक ॥\n" + "\n".join(d['shloka']))
        if d.get('chaupais') and len(d['chaupais']) > 0:
            content_parts.append("॥ चौपाई ॥\n" + "\n".join(d['chaupais']))
        if d.get('chhand') and len(d['chhand']) > 0:
            content_parts.append("॥ छन्द ॥\n" + "\n".join(d['chhand']))
        if d.get('doha') and len(d['doha']) > 0:
            content_parts.append(f"॥ दोहा {doha_num} ॥\n" + "\n".join(d['doha']))
        if d.get('meaning'):
            content_parts.append("॥ पावन हिन्दी भावार्थ ॥\n" + d['meaning'])

        full_content = "\n\n".join(content_parts)
        short_desc = f"{d.get('chapter_title', '')} • {d.get('meaning', '')[:120]}..."
        thumb = d.get('thumb') or 'assets/gallery/bal_hanuman.jpg'
        tags = json.dumps(["सुंदरकांड", "हनुमान", "रामचरितमानस", f"दोहा {doha_num}"], ensure_ascii=False)
        content_hash = hashlib.sha256(f"{item_id}_{full_content}".encode('utf-8')).hexdigest()
        search_kw = f"सुंदरकांड सुन्दरकाण्ड हनुमान रामचरितमानस दोहा {doha_num} {d['title']} {d.get('chapter_title', '')}"

        # Check existing
        cur.execute("SELECT id FROM content_items WHERE id = ?", (item_id,))
        exists = cur.fetchone()

        if exists:
            cur.execute("""
                UPDATE content_items
                SET title = ?, title_en = ?, deity_id = 'hanuman', category_id = 'katha',
                    content_type = 'sundarkand', language = 'hi', short_description = ?,
                    content = ?, thumbnail = ?, duration = 180, tags = ?,
                    is_popular = 1, is_featured = 1, is_trending = 1, status = 'published',
                    content_hash = ?, search_keywords = ?, updated_at = ?
                WHERE id = ?
            """, (title_hi, title_en, short_desc, full_content, thumb, tags, content_hash, search_kw, now, item_id))
            updated_count += 1
        else:
            cur.execute("""
                INSERT INTO content_items (
                    id, title, title_en, deity_id, category_id, content_type,
                    language, short_description, content, thumbnail, audio_url,
                    video_url, duration, tags, is_popular, is_featured, is_trending,
                    status, content_hash, search_keywords, view_count, play_count,
                    share_count, created_at, updated_at
                ) VALUES (
                    ?, ?, ?, 'hanuman', 'katha', 'sundarkand',
                    'hi', ?, ?, ?, '',
                    '', 180, ?, 1, 1, 1,
                    'published', ?, ?, 0, 0,
                    0, ?, ?
                )
            """, (item_id, title_hi, title_en, short_desc, full_content, thumb, tags, content_hash, search_kw, now, now))
            inserted_count += 1

    conn.commit()
    print(f"✓ Completed: Inserted {inserted_count}, Updated {updated_count} Sundarkand dohas.")

    # Verification
    cur.execute("SELECT count(*) FROM content_items WHERE content_type = 'sundarkand'")
    cnt = cur.fetchone()[0]
    print(f"✓ Verified content_items count for 'sundarkand': {cnt}")

    conn.close()

if __name__ == '__main__':
    main()
