from flask import Flask, Blueprint, request, jsonify
import os
# Blueprint for news content
news_routes = Blueprint('news', __name__)
# Define endpoints for each user selection
@news_routes.route('/generate', methods=['POST'])

def generate_content_endpoint():
    data = request.json
    query = data.get('query')
    content_type = data.get('content_type')
    # if not query or not content_type:
    #     return jsonify({"error": "Both 'query' and 'content_type' are required."}), 400
    # response = generate_content(content_type, query) # To do
    # return jsonify(response)

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
