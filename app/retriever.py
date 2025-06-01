from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import faiss
from .pdf_loader import load_all_pdfs

model = SentenceTransformer("all-MiniLM-L6-v2")
docs, filenames = load_all_pdfs()
chunks = []
doc_map = []

for i, doc in enumerate(docs):
    for j in range(0, len(doc), 500):
        chunk = doc[j:j+500]
        if chunk.strip():
            chunks.append(chunk)
            doc_map.append(filenames[i])

embeddings = model.encode(chunks)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

def retrieve_context(query, top_k=5, threshold=0.5):
    query_embedding = model.encode([query])
    D, I = index.search(query_embedding, top_k)
    
    best_chunks = []
    for i, score in zip(I[0], D[0]):
        sim = 1 - score / 4  # crude similarity
        if sim > threshold:
            best_chunks.append(chunks[i])

    return " ".join(best_chunks), len(best_chunks) > 0