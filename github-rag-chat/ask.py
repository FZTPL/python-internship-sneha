import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

import faiss
import pickle
import numpy as np
import subprocess
import sys

print("1. Loaded imports")

index = faiss.read_index("faiss_index.bin")
print("2. Loaded FAISS")

with open("chunks.pkl", "rb") as f:
    chunks = pickle.load(f)
print("3. Loaded chunks")

question = input("Ask a question: ")
print("Question:", repr(question))

# Run embedding in a separate process
subprocess.run([sys.executable, "emb.py", question], check=True)
question_embedding = np.load("/tmp/embedding.npy").astype("float32")
print("5. Embedding created!")

D, I = index.search(question_embedding, k=3)
print("6. Searched FAISS")

context = ""
for idx in I[0]:
    context += chunks[idx] + "\n\n"

print("Context length:", len(context))
print("\nFirst 500 characters:")
print(context[:500])

from gemini import ask_gemini
print("\nCalling Gemini...")
answer = ask_gemini(context, question)
print("Returned from Gemini!")
print(answer)
print("Program finished!")