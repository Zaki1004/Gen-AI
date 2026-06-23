from pathlib import Path

from langchain_community.document_loaders import (
    PyMuPDFLoader
)

PDF_FOLDER = Path(
    "knowledge"
)


def load_all_pdfs():

    documents = []

    pdf_files = (
        PDF_FOLDER.glob("*.pdf")
    )

    for pdf_file in pdf_files:

        loader = PyMuPDFLoader(
            str(pdf_file)
        )

        docs = loader.load()

        documents.extend(
            docs
        )

    return documents