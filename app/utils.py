import requests
from config import GEMINI_API_KEY, GEMINI_URL

def call_gemini_api(prompt):
    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }
    response = requests.post(
        f"{GEMINI_URL}?key={GEMINI_API_KEY}",
        json=payload
    )

    if response.status_code == 200:
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    else:
        print("API Key:", GEMINI_API_KEY)
        print("Gemini API call failed:")
        print("Status code:", response.status_code)
        print("Response body:", response.text)
        return "Error: LLM API call failed."

def improve_response(initial_answer):
    prompt = f"""
Please rewrite and improve the answer below. Make it concise, to the point. Retain all essential details and key concepts, 
organize it clearly in paragraphs and bullet points when needed, and use professional yet accessible language.

Answer to improve:
{initial_answer}
"""
    return call_gemini_api(prompt)