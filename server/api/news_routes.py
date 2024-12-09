from flask import Blueprint, request, jsonify
from api.content_generator import generate_content
import os

# Blueprint for news content
news_routes = Blueprint('news', __name__)

# Define endpoints 
@news_routes.route('/generate', methods=['POST'])
def generate_content_endpoint():
    data = request.json
    query = data.get('query')
    content_type = data.get('content_type')
    platform_type = data.get('platform_type')

    if not query or not content_type or not platform_type:
        return jsonify({"error": "'query','content_type' and 'platform_type' are required."}), 400
    response = generate_content(content_type, query, platform_type) 
    return response, 200

@news_routes.route('/video', methods=['POST'])
def generate_video():
    data = request.json
    query = data.get('query')
    content_type = data.get('content_type')
    response = generate_content(content_type, query)
    return jsonify(response)

@news_routes.route('/meme', methods=['POST'])
def generate_meme():
    data = request.json
    query = data.get('query')
    content_type = data.get('content_type')
    response = generate_content(content_type, query)
    return jsonify(response)

@news_routes.route('/generate_all', methods=['POST'])
def generate_all():
    data = request.json
    query = data.get('query')
    content_type = data.get('content_type')
    response = generate_content(content_type, query)
    return jsonify(response)
