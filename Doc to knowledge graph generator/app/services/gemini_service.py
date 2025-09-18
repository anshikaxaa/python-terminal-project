import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def extract_entities(text: str) -> dict:
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"""
    Extract entities from the following text and return them in JSON format.
    Entities should include: persons, organizations, locations, dates, and other relevant entities.
    Also, identify relationships between entities if possible.

    Text: {text}

    Return format:
    {{
        "entities": [
            {{"type": "PERSON", "value": "John Doe"}},
            {{"type": "ORGANIZATION", "value": "Google"}},
            ...
        ],
        "relationships": [
            {{"subject": "John Doe", "relation": "works at", "object": "Google"}},
            ...
        ]
    }}
    """
    response = model.generate_content(prompt)
    # Assuming the response is JSON, parse it
    import json
    try:
        return json.loads(response.text)
    except:
        return {"entities": [], "relationships": []}
