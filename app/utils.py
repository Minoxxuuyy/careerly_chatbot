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
Please improve the answer below by:
1. Expanding it with more comprehensive information and relevant details
2. Including key concepts, examples, or applications where appropriate
3. Ensuring it remains accurate and directly addresses the question
4. Organizing the information in a clear, structured manner with multiple paragraphs for different aspects of the topic
5. Using professional yet accessible language
6. Aim for a response of 3-5 paragraphs that thoroughly explores the topic

Answer:
{initial_answer}
"""
    return call_gemini_api(prompt)