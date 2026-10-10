# ====================================================================
# BHAKTI APP: SCHEMA & DATA VALIDATOR
# ====================================================================

from typing import Dict, Any, List, Tuple
from .models import ContentType, Deity, ContentStatus

VALID_CONTENT_TYPES = {t.value for t in ContentType}
VALID_DEITIES = {d.value for d in Deity}
VALID_STATUSES = {s.value for s in ContentStatus}

REQUIRED_FIELDS = ['title', 'deity_id', 'content_type', 'content']

def validate_content_data(data: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """
    Validates a raw dictionary representing a content item.
    Returns (is_valid: bool, errors: List[str]).
    """
    errors = []

    # Check required fields
    for f in REQUIRED_FIELDS:
        if f not in data or not str(data[f]).strip():
            errors.append(f"Missing required field: '{f}'")

    # Validate content_type
    ctype = str(data.get('content_type', '')).strip().lower()
    if ctype and ctype not in VALID_CONTENT_TYPES:
        errors.append(f"Invalid content_type '{ctype}'. Allowed: {', '.join(sorted(VALID_CONTENT_TYPES))}")

    # Validate deity_id
    deity = str(data.get('deity_id', '')).strip().lower()
    if deity and deity not in VALID_DEITIES:
        errors.append(f"Invalid deity_id '{deity}'. Allowed: {', '.join(sorted(VALID_DEITIES))}")

    # Validate status if provided
    status = str(data.get('status', 'published')).strip().lower()
    if status and status not in VALID_STATUSES:
        errors.append(f"Invalid status '{status}'. Allowed: draft, published, archived")

    # Validate duration
    duration = data.get('duration', 0)
    try:
        dur_int = int(duration)
        if dur_int < 0:
            errors.append("Duration must be a positive number of seconds.")
    except (ValueError, TypeError):
        errors.append("Duration must be an integer (in seconds).")

    return (len(errors) == 0, errors)
