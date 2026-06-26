from sentence_transformers import SentenceTransformer
from read_files import read_repository
import faiss
import numpy as np


documents = read_repository("repos/project")


chunks = []
chunk_size = 500

for doc in documents:
    for i in range(0, len(doc), chunk_size):
        chunks.append(doc[i:i + chunk_size])


model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(chunks)

embeddings = np.array(embeddings, dtype="float32")


dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

import pickle

faiss.write_index(index,
    "faiss_index.bin"
)

with open(
    "chunks.pkl",
    "wb"
) as f:
    pickle.dump(
        chunks,
        f
    )

print("Saved!")