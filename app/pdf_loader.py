import os
import PyPDF2

def load_all_pdfs(data_dir="data/fields/"):
    docs = []
    filenames = []
    for fname in os.listdir(data_dir):
        if fname.endswith(".pdf"):
            path = os.path.join(data_dir, fname)
            with open(path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                text = " ".join(page.extract_text() or "" for page in reader.pages)
                docs.append(text)
                filenames.append(fname)
    return docs, filenames