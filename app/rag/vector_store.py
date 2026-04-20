import faiss
import numpy as np
import os

dimension = 384
index_file = "faiss_index.bin"
doc_file = "documents.pkl"

# Load if exists
if os.path.exists(index_file):
    index = faiss.read_index(index_file)
else:
    index = faiss.IndexFlatL2(dimension)

# Store documents
if os.path.exists(doc_file):
    import pickle
    with open(doc_file, "rb") as f:
        documents = pickle.load(f)
else:
    documents = []

def add_document(text, vector):
    index.add(np.array([vector]))
    documents.append(text)

def save():
    faiss.write_index(index, index_file)
    import pickle
    with open(doc_file, "wb") as f:
        pickle.dump(documents, f)

def search(vector, k=3):
    if index.ntotal == 0:
        return []

    D, I = index.search(np.array([vector]), k)
    return [documents[i] for i in I[0] if i < len(documents)]


if __name__ == "__main__":
    print("Total vectors:", index.ntotal)