from agents.news_agents import crew
from flask import jsonify

def generate_content(content_type, query, platform_type):
   
    if content_type == "text":
        try:
            result = crew.kickoff(inputs={"topic": query, "platform": platform_type})
            return result
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    elif content_type == "image":
        return {"type": "image", "content": f"Generated image for query: {query}"}
    elif content_type == "video":
        return {"type": "video", "content": f"Generated video for query: {query}"}
    elif content_type == "meme":
        return {"type": "meme", "content": f"Generated meme for query: {query}"}
    elif content_type == "all":
        return {
            "type": "all",
            "content": {
                "text": f"Text post for query: {query}",
                "image": f"Generated image for query: {query}",
                "video": f"Generated video for query: {query}",
                "meme": f"Generated meme for query: {query}"
            }
        }


















# # Load OpenAI API key
# openai.api_key = os.getenv("OPENAI_API_KEY")

# def generate_response(query):
#     """
#     Generate text and image responses using OpenAI GPT and DALL-E.
#     """
#     # Generate text response
#     completion = openai.ChatCompletion.create(
#         model="gpt-4",
#         messages=[{"role": "user", "content": query}]
#     )
#     response_text = completion.choices[0].message.content

#     # Generate image using DALL-E
#     image_response = openai.Image.create(
#         prompt=query,
#         n=1,
#         size="1024x1024"
#     )
#     image_url = image_response['data'][0]['url']

#     return jsonify({'text': response_text, 'image': image_url})



# user_posts= Blueprit('user_posts', __name__)

# # Load OpenAI API key
# openai.api_key = os.getenv("OPENAI_API_KEY")

# def generate_response(query):
#     """
#     Generate text and image responses using OpenAI GPT and DALL-E.
#     """
#     # Generate text response
#     completion = openai.ChatCompletion.create(
#         model="gpt-4",
#         messages=[{"role": "user", "content": query}]
#     )
#     response_text = completion.choices[0].message.content

#     # Generate image using DALL-E
#     image_response = openai.Image.create(
#         prompt=query,
#         n=1,
#         size="256x256"
#     )
#     image_url = image_response['data'][0]['url']

#     return jsonify({'text': response_text, 'image': image_url})


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
