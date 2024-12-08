from flask import Blueprint, request, jsonify
import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")  #set your key directly, "your-api-key-here"

api_bp = Blueprint('api', __name__)

# Text generation using GPT-4
@api_bp.route('/user-query', methods=['POST'])
def user_query():
    data = request.get_json()
    if not data or 'query' not in data:
        return jsonify({'error': 'Query is required'}), 400

    query = data['query']

    # Request text response from GPT-4 API
    try:
        response = openai.Completion.create(
            model="gpt-4",  # Use GPT-4 model
            prompt=query,
            max_tokens=200,  # Adjust as needed
            temperature=0.6,  # Adjust for more or less creativity
            top_p=1,  # Controls the diversity of the output
            frequency_penalty=0,  # Adjust if you want to penalize frequent words
            presence_penalty=0  # Adjust if you want to penalize words appearing in the context
        )
        response_text = response.choices[0].text.strip()

        return jsonify({
            'text': response_text
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Image generation using DALL·E
@api_bp.route('/generate-image', methods=['POST'])
def generate_image():
    data = request.get_json()
    if not data or 'query' not in data:
        return jsonify({'error': 'Query is required'}), 400

    query = data['query']

    try:
        # Request image generation from DALL·E API
        response = openai.Image.create(
            prompt=query,
            n=1,  # Number of images to generate
            size="1024x1024"  # Size of the image (you can adjust)
        )
        
        # Get the image URL from the response
        image_url = response['data'][0]['url']

        return jsonify({
            'image_url': image_url
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# from flask import Blueprint, request, jsonify
# api_bp = Blueprint('api', __name__)

# @api_bp.route('/user-query', methods=['POST'])
# def user_query():
#     data = request.get_json()
#     if not data or 'query' not in data:
#         return jsonify({'error': 'Query is required'}), 400
#     query = data['query']
#     return generate_response(query)
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

# def generate_image_url(query):
#     """
#     Generates a placeholder or a query-based image URL.
#     """
#     # Simple mock logic for now
#     if "AI" in query:
#         return "https://via.placeholder.com/150?text=AI"
#     return "https://via.placeholder.com/150?text=Query+Response"
