import google.generativeai as genai
import json

def create_itinerary(name):
    GOOGLE_API_KEY="AIzaSyA7yE_H6thblojL7FtlbbDDNWOwaIYNC5c"
    genai.configure(api_key=GOOGLE_API_KEY)
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
        generation_config=generation_config
    )

    prompt = f"""
    Create an itinerary for a person travelling to {name} using this JSON schema:
        Place = {{ "time": str, "location": str }}
    Return a `list[Place]`
    """

    response = model.generate_content(prompt)
    output = json.loads(response.text)
    return output
