# ====================================================================
# BHAKTI APP: DEDUPLICATION & CONTENT HASH ENGINE
# ====================================================================

import re
import hashlib
import sqlite3
from typing import Optional, Tuple
from .normalizer import normalize_devanagari

def generate_content_hash(title: str, deity_id: str, content_type: str) -> str:
    clean_title = normalize_devanagari(title).strip().lower()
    clean_title_alphanumeric = re.sub(r'[^\w]', '', clean_title, flags=re.UNICODE)
    
    clean_deity = deity_id.strip().lower()
    clean_type = content_type.strip().lower()
    
    raw_signature = f"{clean_title_alphanumeric}|{clean_deity}|{clean_type}"
    return hashlib.sha256(raw_signature.encode('utf-8')).hexdigest()

def generate_slug(content_type: str, deity_id: str, title: str) -> str:
    clean_title = re.sub(r'[^a-zA-Z0-9\u0900-\u097F\s_-]', '', title).strip().lower()
    clean_title = re.sub(r'\s+', '-', clean_title)
    slug = f"{content_type.strip().lower()}-{deity_id.strip().lower()}-{clean_title}"
    return slug[:80].rstrip('-')

def check_duplicate(conn: sqlite3.Connection, content_hash: str) -> Optional[Tuple[str, str]]:
    cursor = conn.cursor()
    cursor.execute("SELECT id, title FROM content_items WHERE content_hash = ?", (content_hash,))
    row = cursor.fetchone()
    if row:
        return (row[0], row[1])
    return None
