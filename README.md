# Algerian university Fields information Chatbot (AI RAG Chatbot)

This is a Flask-based AI chatbot that uses Retrieval-Augmented Generation (RAG) to answer questions about university fields in Algeria. Each field is associated with a PDF file containing information such as curriculum, universities, and job opportunities.

## Features

- Retrieval-Augmented Generation (RAG)
- Uses Gemini Pro (Google Generative Language API)
- Answers domain-specific questions from PDFs (for now 5 pdfs are considered as we have five fields only)
- Two-step response:
  1. Retrieve + generate raw answer
  2. Improve final response with high-quality formatting
- Deployable for free on Render.com


## Architecture Overview

1. **PDF Parsing**: Extracts content from each field PDF.
2. **Chunking**: Each document is split into ~500-character chunks.
3. **Embedding**: Embeddings are generated using `MiniLM-L6` from SentenceTransformers.
4. **FAISS Index**: In-memory vector search is used to find relevant chunks for a given question.
5. **LLM Call**:
   - First call: Generate a basic response using relevant chunks.
   - Second call: Improve the response (more detailed, structured, and professional).

---

## Project Structure
ai_chatbot/
│
├── app/
│   ├── init.py               
│   ├── routes.py             # Flask routes
│   ├── chatbot.py            # Chatbot logic
│   ├── retriever.py          # Vector search logic (FAISS)
│   ├── pdf_loader.py         # PDF parsing
│   └── utils.py              # Gemini API calls
│
├── data/
│   └── fields/               # PDF files ( e.g. medicine.pdf)
│
├── main.py                   # Entry point
├── config.py                 # Config & keys
├── requirements.txt
├── Procfile                  # For Render deployment
└── README.md
