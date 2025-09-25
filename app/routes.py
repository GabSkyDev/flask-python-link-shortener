from flask import Blueprint, request, jsonify, redirect
from .services import save_url, get_original_url

bp = Blueprint("main", __name__)

@bp.route("/shorten", methods=["POST"])
def shorten():
    data = request.get_json()
    original_url = data.get("url")

    if not original_url:
        return jsonify({"error": "URL é obrigatória"}), 400
    
    short_id = save_url(original_url)
    return jsonify({"short_url": f"http://localhost:5000/{short_id}"})

@bp.route("/<short_id>")
def redirect_to_url(short_id):
    url = get_original_url(short_id)
    if url:
        return redirect(url)
    return jsonify({"error": "URL não encontrada"}), 404