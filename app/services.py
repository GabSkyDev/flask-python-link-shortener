import hashlib
from .models import URL
from . import db

def generate_short_id(url: str) -> str:
    return hashlib.md5(url.encode()).hexdigest()[:6]

def save_url(original_url: str) -> str:
    short_id = generate_short_id(original_url)
    url_entry = URL(original_url=original_url, short_id=short_id)
    db.session.add(url_entry)
    db.session.commit()
    return short_id

def get_original_url(short_id: str) -> str | None:
    url_entry = URL.query.filter_by(short_id=short_id).first()
    return url_entry.original_url if url_entry else None