from flask import Blueprint, request, jsonify
api_bp = Blueprint('api', __name__)

@api_bp.route('/user-query', methods=['POST'])
def user_query():
    data = request.get_json()
    if not data or 'query' not in data:
        return jsonify({'error': 'Query is required'}), 400
    query = data['query']
    return generate_response(query)
# def user_query():
#     data = request.get_json()
#     if not data or 'query' not in data:
#         return jsonify({'error': 'Query is required'}), 400

#     query = data['query']
    
#     # Generate response
#     response_text = f'You asked: "{query}"'
    
#     # Replace this logic with actual image generation or URL fetching
#     image_url = generate_image_url(query)

#     return jsonify({
#         'text': response_text,
#         'image': image_url
#     })

def generate_image_url(query):
    """
    Generates a placeholder or a query-based image URL.
    """
    # Simple mock logic for now
    if "AI" in query:
        return "https://via.placeholder.com/150?text=AI"
    return "https://via.placeholder.com/150?text=Query+Response"
