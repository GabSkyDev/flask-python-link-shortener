from app.models import URL, db

def test_create_url(app):
    url = URL(original_url="https://example.com", short_id="abc123")
    db.session.add(url)
    db.session.commit()

    found = URL.query.filter_by(short_id="abc123").first()
    assert found is not None
    assert found.original_url == "https://example.com"