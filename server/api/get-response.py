from flask import jsonify
import openai
import os
def generate_response(query):
    response_text = generate_text_response(query)
    image_url = generate_image_url(query)
    return jsonify({'text': response_text, 'image': image_url})

def generate_text_response(query):
    try:
        response = openai.Completion.create(
            model="gpt-4",  
            prompt=query,
            max_tokens=100
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error generating text: {str(e)}"

def generate_image_url(query):
    try:
        response = openai.Image.create(
            prompt=query,
            n=1,
            size="256x256"
        )
        return response['data'][0]['url']
    except Exception as e:
        return f"Error generating image: {str(e)}"

