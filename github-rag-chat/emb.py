import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

import sys
import numpy as np
from sentence_transformers import SentenceTransformer

question = sys.argv[1]
model = SentenceTransformer("all-MiniLM-L6-v2")
embedding = model.encode([question])
np.save("/tmp/embedding.npy", embedding)