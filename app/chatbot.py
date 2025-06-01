from .retriever import retrieve_context
from .utils import call_gemini_api, improve_response

def generate_final_response(question):
    chunks, relevant = retrieve_context(question)

    if not relevant:
        return "Sorry, I'm not able to answer that. My scope is limited to Algerian university fields."

    prompt = f"""You are a helpful academic assistant.
Context: {chunks}
Question: {question}
Answer:"""
    
    initial_response = call_gemini_api(prompt)
    final_response = improve_response(initial_response)

    return final_response