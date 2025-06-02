from .retriever import retrieve_context
from .utils import call_gemini_api, improve_response

def generate_final_response(question):
    chunks, relevant = retrieve_context(question)

    if not relevant:
        base_prompt = f"""You are a helpful academic assistant. 
Provide a concise, brief and accurate answer to the following question:
Question: {question}
Answer:"""
        initial_response = call_gemini_api(base_prompt)
        return improve_response(initial_response)

    # Otherwise, include context as before
    full_prompt = f"""You are a helpful academic assistant.
Context: {chunks}
Question: {question}
Answer:"""
    initial_response = call_gemini_api(full_prompt)
    final_response = improve_response(initial_response)
    return final_response