def test_shorten_and_redirect(client):
    # 1) cria URL encurtada
    response = client.post("/shorten", json={"url": "https://example.com"})
    assert response.status_code == 200

    data = response.get_json()
    assert "short_url" in data

    # 2) extrai o short_id da resposta
    short_url = data["short_url"]        # ex: http://localhost:5000/abc123
    short_id = short_url.rsplit("/", 1)[-1]

    # 3) tenta acessar a rota de redirecionamento
    redirect_response = client.get(f"/{short_id}")
    # Flask test client não segue redirect automaticamente,
    # então checamos o header "Location"
    assert redirect_response.status_code == 302
    assert redirect_response.headers["Location"] == "https://example.com"

def test_shorten_without_url(client):
    # envia JSON sem "url"
    response = client.post("/shorten", json={})
    assert response.status_code == 400

    data = response.get_json()
    assert "error" in data
    assert data["error"] == "URL é obrigatória"