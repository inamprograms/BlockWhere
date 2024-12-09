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
        # Call the `generate_image` function and return the result
        image_result = generate_image(query)
        if isinstance(image_result, str):  # If a valid Base64 string
            return {"type": "image", "content": f"data:image/png;base64,{image_result}"}
        else:
            return jsonify(image_result), 500

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


def generate_image(query):
    api_url = "https://api.openai.com/v1/images/generations"  # OpenAI DALL·E API URL
    api_key =  os.getenv("OPENAI_API_KEY")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "prompt": query, 
        "n": 1,  # Number of images to generate
        "size": "1024x1024" 
    }

    try:
        # Send the request to the OpenAI image generation API
        response = requests.post(api_url, json=payload, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Get the URL of the generated image from the response
            image_url = response.json()['data'][0]['url']
            print(f"Image URL: {image_url}")  # Debugging: print the image URL

            # Fetch the image from the URL
            image_response = requests.get(image_url)
            image = Image.open(BytesIO(image_response.content))  # Open the image

            # Optionally, save or display the image
            image.save("generated_image.png")
            return image
        else:
            print(f"Error: {response.status_code} - {response.text}")  # Debugging: print the error
            return {"error": f"Error generating image: {response.status_code} - {response.text}"}
    except Exception as e:
        print(f"An error occurred: {str(e)}")  # Debugging: print exception details
        return {"error": f"An error occurred: {str(e)}"}

# Get user input for the query
user_query = input("Enter a description for the image you want to generate: ")

# Generate the image
generated_image = generate_image(user_query)

# Check if the result is an image or an error dictionary
if isinstance(generated_image, Image.Image):
    # Display the generated image
    print("Image generated successfully! Displaying it now...")
    generated_image.show()
else:
    # Print the error message
    print("Failed to generate image:", generated_image)
