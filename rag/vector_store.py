from pathlib import Path

import faiss
import pickle
import numpy as np


VECTOR_DIR = Path(
    "vectorstore"
)

VECTOR_DIR.mkdir(
    exist_ok=True
)


def save_faiss_index(
    embeddings,
    chunks
):

    dimension = len(
        embeddings[0]
    )

    index = faiss.IndexFlatL2(
        dimension
    )

    vectors = np.array(
        embeddings,
        dtype="float32"
    )

    index.add(
        vectors
    )

    faiss.write_index(
        index,
        str(
            VECTOR_DIR /
            "coffeebot.index"
        )
    )

    with open(
        VECTOR_DIR /
        "chunks.pkl",
        "wb"
    ) as f:

        pickle.dump(
            chunks,
            f
        )

    return index

def load_faiss_index():

    index = faiss.read_index(
        str(
            VECTOR_DIR /
            "coffeebot.index"
        )
    )

    with open(
        VECTOR_DIR /
        "chunks.pkl",
        "rb"
    ) as f:

        chunks = pickle.load(f)

    return index, chunks