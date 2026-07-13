from sentence_transformers import SentenceTransformer

print("=== IMPORT RETRIEVER START ===")

MODEL_NAME = "all-MiniLM-L6-v2"

print("Loading SentenceTransformer...")

embedding_model = SentenceTransformer(MODEL_NAME)

print("SentenceTransformer loaded.")

from rag.vector_store import load_faiss_index
from rag.query_expansion import expand_query

print("Retriever imported successfully.")