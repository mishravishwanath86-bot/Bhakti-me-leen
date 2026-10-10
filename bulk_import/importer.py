import sys
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass
# ====================================================================
# BHAKTI APP: BULK IMPORT ENGINE (JSON & CSV SUPPORT)
# Scalability: Imports 5,000+ to 50,000+ items with batch deduplication
# ====================================================================

import os
import sys
import json
import csv
import argparse
from typing import List, Dict, Any

# Add project root to sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.database import BhaktiDB
from core.validator import validate_content_data

def load_from_json(file_path: str) -> List[Dict[str, Any]]:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, dict) and "items" in data:
        return data["items"]
    elif isinstance(data, list):
        return data
    else:
        raise ValueError("JSON must contain an array of objects or an object with an 'items' key.")

def load_from_csv(file_path: str) -> List[Dict[str, Any]]:
    items = []
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Parse boolean flags
            for bool_key in ['is_popular', 'is_featured', 'is_trending']:
                if bool_key in row:
                    val = str(row[bool_key]).strip().lower()
                    row[bool_key] = val in ('1', 'true', 'yes', 'y')

            # Parse tags
            if 'tags' in row and row['tags']:
                tags_str = str(row['tags']).strip()
                if tags_str.startswith('[') and tags_str.endswith(']'):
                    try: row['tags'] = json.loads(tags_str)
                    except: row['tags'] = [t.strip() for t in tags_str[1:-1].split(',') if t.strip()]
                else:
                    row['tags'] = [t.strip() for t in tags_str.split(',') if t.strip()]
            else:
                row['tags'] = []

            # Parse duration
            if 'duration' in row:
                try: row['duration'] = int(row['duration'])
                except: row['duration'] = 0

            items.append(row)
    return items

def run_bulk_import(
    file_path: str,
    db_path: str = None,
    on_duplicate: str = 'skip',
    dry_run: bool = False
) -> Dict[str, Any]:
    """
    Executes bulk import from JSON or CSV.
    on_duplicate: 'skip' | 'overwrite' | 'error'
    """
    if not os.path.exists(file_path):
        return {'success': False, 'error': f"File not found: {file_path}"}

    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.json':
        items = load_from_json(file_path)
    elif ext == '.csv':
        items = load_from_csv(file_path)
    else:
        return {'success': False, 'error': f"Unsupported file extension '{ext}'. Use .json or .csv"}

    print(f"Loaded {len(items)} items from {file_path}")

    # Validate items
    valid_items = []
    validation_errors = []
    for idx, item in enumerate(items):
        is_valid, errors = validate_content_data(item)
        if not is_valid:
            validation_errors.append(f"Row {idx+1} '{item.get('title', 'Unknown')}': {', '.join(errors)}")
        else:
            valid_items.append(item)

    if validation_errors:
        print(f"⚠️ Validation warnings for {len(validation_errors)} rows:")
        for err in validation_errors[:10]:
            print(f"  - {err}")
        if len(validation_errors) > 10:
            print(f"  ... and {len(validation_errors) - 10} more.")

    if dry_run:
        return {
            'success': True,
            'dry_run': True,
            'total_items': len(items),
            'valid_count': len(valid_items),
            'invalid_count': len(validation_errors),
            'validation_errors': validation_errors[:50]
        }

    # Execute DB batch insert
    db = BhaktiDB(db_path=db_path) if db_path else BhaktiDB()
    result = db.bulk_insert(valid_items, on_duplicate=on_duplicate)
    result['validation_errors_count'] = len(validation_errors)
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Bhakti App Bulk Content Importer")
    parser.add_argument("--file", required=True, help="Path to JSON or CSV file")
    parser.add_argument("--on-duplicate", choices=['skip', 'overwrite', 'error'], default='skip', help="Duplicate resolution")
    parser.add_argument("--dry-run", action="store_true", help="Validate without writing to database")
    args = parser.parse_args()

    res = run_bulk_import(args.file, on_duplicate=args.on_duplicate, dry_run=args.dry_run)
    print("\n=== Import Result ===")
    print(json.dumps(res, indent=2, ensure_ascii=False))
