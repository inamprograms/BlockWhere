from flask import jsonify

def generate_response(query):
    # Generate response text and image URL
    response_text = f'You asked: "{query}"'
    image_url = generate_image_url(query)
    return jsonify({'text': response_text, 'image': image_url})

def generate_image_url(query):
    if "AI" in query:
        return "https://via.placeholder.com/150?text=AI"
    return "https://via.placeholder.com/150?text=Query+Response"
