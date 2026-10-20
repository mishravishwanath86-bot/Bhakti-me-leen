# ====================================================================
# BHAKTI APP: REST API CONTROLLER (SECURITY HARDENED)
# Connects HTTP Requests to Database Engine with JSON Responses
# ====================================================================

import os
import re
import json
import time
import traceback
import urllib.parse
from typing import Dict, Any, Tuple, Optional, List
from db.database import BhaktiDB
from core.validator import validate_content_data
from bulk_import.importer import run_bulk_import
from core.ai_audio_engine import generate_ai_bhakti_audio, AI_AUDIO_DIR

db = BhaktiDB()

# --------------------------------------------------------------------
# SECURITY GUARD 1: ADMIN AUTHENTICATION
# --------------------------------------------------------------------
ADMIN_SECRET_KEY = os.environ.get("BHAKTI_ADMIN_KEY", "bhakti_admin_key_2026")

def verify_admin_auth(headers: Optional[Dict[str, str]], query_params: Dict[str, str]) -> bool:
    """
    Verifies admin authorization from headers (X-Admin-Key, Authorization) or query parameters.
    """
    if not headers:
        headers = {}
    h_lower = {str(k).lower(): str(v) for k, v in headers.items()}

    # 1. Header: X-Admin-Key
    if h_lower.get('x-admin-key') == ADMIN_SECRET_KEY:
        return True

    # 2. Header: Authorization Bearer
    auth = h_lower.get('authorization', '')
    if auth.startswith('Bearer ') and auth[7:].strip() == ADMIN_SECRET_KEY:
        return True

    # 3. Query Param: admin_key or api_key
    if query_params.get('admin_key') == ADMIN_SECRET_KEY or query_params.get('api_key') == ADMIN_SECRET_KEY:
        return True

    return False

# --------------------------------------------------------------------
# SECURITY GUARD 2: IN-MEMORY SLIDING WINDOW RATE LIMITER
# --------------------------------------------------------------------
_rate_limit_cache: Dict[str, List[float]] = {}

def is_rate_limited(client_ip: str, action: str, max_calls: int = 5, window_sec: int = 60) -> Tuple[bool, int]:
    """
    Returns (is_limited, retry_after_seconds)
    """
    now = time.time()
    key = f"{client_ip}:{action}"
    timestamps = _rate_limit_cache.get(key, [])
    # Keep timestamps within active window
    timestamps = [t for t in timestamps if now - t < window_sec]
    if len(timestamps) >= max_calls:
        retry_after = int(window_sec - (now - timestamps[0])) + 1
        _rate_limit_cache[key] = timestamps
        return True, max(1, retry_after)
    timestamps.append(now)
    _rate_limit_cache[key] = timestamps
    return False, 0

# --------------------------------------------------------------------
# SECURITY GUARD 3: INPUT SANITIZATION HELPER
# --------------------------------------------------------------------
def sanitize_input_text(text: Any) -> str:
    """Strips executable script tags and dangerous HTML attributes."""
    if not isinstance(text, str):
        return ""
    # Strip script and style tags
    clean = re.sub(r'<script.*?>.*?</script>', '', text, flags=re.IGNORECASE | re.DOTALL)
    clean = re.sub(r'<style.*?>.*?</style>', '', clean, flags=re.IGNORECASE | re.DOTALL)
    clean = re.sub(r'on\w+="[^"]*"', '', clean, flags=re.IGNORECASE)
    clean = re.sub(r"on\w+='[^']*'", '', clean, flags=re.IGNORECASE)
    return clean.strip()

# --------------------------------------------------------------------
# MAIN API REQUEST DISPATCHER
# --------------------------------------------------------------------
def handle_api_request(
    method: str, 
    path: str, 
    query_params: Dict[str, str], 
    body_data: Any,
    headers: Optional[Dict[str, str]] = None,
    client_ip: str = "127.0.0.1"
) -> Tuple[int, str, bytes]:
    """
    Dispatches API requests with Security Gates and returns (status_code, content_type, response_bytes).
    """
    headers_ct = "application/json; charset=utf-8"

    try:
        # SECURITY ENFORCEMENT: Protect all Admin endpoints (/api/admin/*)
        if path.startswith("/api/admin/"):
            if not verify_admin_auth(headers, query_params):
                return (401, headers_ct, json.dumps({
                    'success': False,
                    'error': 'अनधिकृत अनुरोध: मान्य Admin API Key आवश्यक है (Unauthorized: Valid Admin API Key required)'
                }, ensure_ascii=False).encode('utf-8'))

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

        # 3. GET /api/content (Paginated List or Single item by id)
        if method == "GET" and path == "/api/content":
            item_id = query_params.get('id')
            if item_id:
                item = db.get_content_by_id(item_id)
                if not item:
                    return (404, headers_ct, json.dumps({'error': 'Item not found'}, ensure_ascii=False).encode('utf-8'))
                return (200, headers_ct, json.dumps(item, ensure_ascii=False).encode('utf-8'))

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
                res = db.search_content(query=sanitize_input_text(q), content_type=ctype, deity_id=deity, status=status, has_audio=has_audio, audio_source=audio_source, limit=limit, page=page)
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
                res = db.search_content(query=sanitize_input_text(q), content_type=ctype, deity_id=deity, has_audio=True, audio_source=source, status=status, limit=limit, page=page)
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

        # 9. POST /api/admin/bulk-import (JSON Payload) - With Rate Limiting
        if method == "POST" and path == "/api/admin/bulk-import":
            if not body_data:
                return (400, headers_ct, json.dumps({'error': 'Missing payload'}).encode('utf-8'))

            is_limited, retry_sec = is_rate_limited(client_ip, "bulk_import", max_calls=10, window_sec=60)
            if is_limited:
                return (429, headers_ct, json.dumps({
                    'success': False,
                    'error': f'अनुरोध सीमा पार: कृपया {retry_sec} सेकंड प्रतीक्षा करें (Rate limit exceeded: wait {retry_sec}s)',
                    'retry_after': retry_sec
                }, ensure_ascii=False).encode('utf-8'))
            
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

        # 10. POST /api/ai-audio/generate - With Rate Limiting & Input Length Protection
        if method == "POST" and path == "/api/ai-audio/generate":
            if not isinstance(body_data, dict):
                return (400, headers_ct, json.dumps({'success': False, 'error': 'Invalid JSON body'}).encode('utf-8'))

            # Rate Limit: max 5 requests per minute per IP
            is_limited, retry_sec = is_rate_limited(client_ip, "ai_audio_gen", max_calls=5, window_sec=60)
            if is_limited:
                return (429, headers_ct, json.dumps({
                    'success': False,
                    'error': f'अनुरोध सीमा पार: AI ऑडियो निर्माण हेतु कृपया {retry_sec} सेकंड प्रतीक्षा करें (Rate limit: wait {retry_sec}s)',
                    'retry_after': retry_sec
                }, ensure_ascii=False).encode('utf-8'))
            
            content_id = body_data.get('content_id') or body_data.get('id') or 'custom'
            text = sanitize_input_text(body_data.get('text') or body_data.get('content') or '')
            title = sanitize_input_text(body_data.get('title') or '')
            content_type = body_data.get('content_type') or body_data.get('type') or 'aarti'
            voice = body_data.get('voice') or 'male'
            speed = float(body_data.get('speed', 1.0))

            if not text:
                return (400, headers_ct, json.dumps({'success': False, 'error': 'टेक्स्ट रिक्त है (Text required)'}, ensure_ascii=False).encode('utf-8'))

            if len(text) > 5000:
                return (400, headers_ct, json.dumps({'success': False, 'error': 'टेक्स्ट सीमा पार (अधिकतम 5000 वर्ण)'}, ensure_ascii=False).encode('utf-8'))

            result = generate_ai_bhakti_audio(
                content_id=str(content_id),
                text=text,
                title=title,
                content_type=content_type,
                voice=voice,
                custom_speed=speed
            )
            status_code = 200 if result.get('success') else 500
            return (status_code, headers_ct, json.dumps(result, ensure_ascii=False).encode('utf-8'))

        # 11. GET /api/ai-audio/status (Check if AI audio exists for content)
        if method == "GET" and path == "/api/ai-audio/status":
            content_id = query_params.get('content_id') or query_params.get('id')
            voice = query_params.get('voice', 'male')
            if not content_id:
                return (400, headers_ct, json.dumps({'error': 'Missing content_id'}).encode('utf-8'))
            
            # Check if any file matches bhakti_{content_id}_{voice}_*.mp3
            prefix = f"bhakti_{content_id}_{voice.lower()}_"
            matched = [f for f in os.listdir(AI_AUDIO_DIR) if f.startswith(prefix) and f.endswith(".mp3")]
            if matched:
                return (200, headers_ct, json.dumps({
                    'exists': True,
                    'audio_url': f"/assets/ai_audio/{matched[0]}",
                    'file_name': matched[0]
                }).encode('utf-8'))
            return (200, headers_ct, json.dumps({'exists': False}).encode('utf-8'))

        return (404, headers_ct, json.dumps({'error': 'Not Found'}).encode('utf-8'))

    # SECURITY GUARD 5: MASK INTERNAL SERVER TRACES IN PRODUCTION
    except Exception as e:
        traceback.print_exc()
        is_debug = os.environ.get("DEBUG", "0") == "1"
        error_msg = str(e) if is_debug else "सर्वर पर आंतरिक तकनीकी समस्या आई। कृपया कुछ समय बाद पुनः प्रयास करें। (Internal Server Error)"
        return (500, headers_ct, json.dumps({'success': False, 'error': error_msg}, ensure_ascii=False).encode('utf-8'))
