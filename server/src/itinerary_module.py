import google.generativeai as genai
import json

GOOGLE_API_KEY = "AIzaSyA7yE_H6thblojL7FtlbbDDNWOwaIYNC5c"
genai.configure(api_key=GOOGLE_API_KEY)


def create_itinerary(name):
    # Create the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "application/json",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    prompt = f"""
    Create an itinerary for a person travelling to {name} using this JSON schema:
        Place = {{ "time": str, "location": str, "website": str, "nearby_hotels": str, "nearby_restaurants": list }}
    Return a list[Place]
    The time must be in 12 hour format, eg 1:00 PM.
    Make sure to include the website URLs of each location, suggest nearby hotels for each place, and provide a list of nearby restaurants. 
    For each restaurant, include its name, type of cuisine (e.g., Italian, Mexican).
    """

    response = model.generate_content(prompt)
    output = json.loads(response.text)
    return output
