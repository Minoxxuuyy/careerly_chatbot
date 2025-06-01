from flask import Blueprint, request, jsonify
from .chatbot import generate_final_response

main = Blueprint('main', __name__)

@main.route("/chat", methods=["POST"])
def chat():
    data = request.json
    question = data.get("question", "")

    if not question:
        return jsonify({"error": "No question provided"}), 400

    response = generate_final_response(question)
    return jsonify({"response": response})