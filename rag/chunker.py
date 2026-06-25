from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

# ======================================
# Chunk Configuration
# ======================================

CHUNK_SIZE = 768

CHUNK_OVERLAP = 100

SEPARATORS = [

    "\n\n",

    "\n",

    ". ",

    " "

]


# ======================================
# Create Chunks
# ======================================

def create_chunks(
    documents
):

    splitter = (
        RecursiveCharacterTextSplitter(

            chunk_size=CHUNK_SIZE,

            chunk_overlap=CHUNK_OVERLAP,

            separators=SEPARATORS

        )
    )

    chunks = splitter.split_documents(
        documents
    )

    return chunks