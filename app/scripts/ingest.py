from app.rag.pdf_loader import load_pdf, chunk_text
from app.rag.embedder import get_embedding
from app.rag.vector_store import add_document

pdf_files = [
    "data/PYTHON UNIT-1 PART I.pdf",
    "data/PYTHON UNIT-1 PART II.pdf",
    "data/PYTHON UNIT-2.pdf",
    "data/PYTHON UNIT-3 (1).pdf",
    "data/PYTHON UNIT-4 (1).pdf",
    "data/PYTHON UNIT-5 (2).pdf"
]

for file in pdf_files:
    print(f"Processing {file}")

    text = load_pdf(file)
    chunks = chunk_text(text)

    for chunk in chunks:
        vec = get_embedding(chunk)
        add_document(chunk, vec)

from app.rag.vector_store import save

save()
print("✅ FAISS index saved")