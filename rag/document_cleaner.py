import re

# ==========================
# Header Patterns
# ==========================

HEADER_PATTERNS = [

    r"Rahasia Candu - Roasting Kopi",

]

# ==========================
# Footer Patterns
# ==========================

FOOTER_PATTERNS = [

    r"Copyright.*",

    r"All Rights Reserved.*",

    r"www\..*",

    r"ISBN.*"

]

# ==========================
# Page Number
# ==========================

PAGE_PATTERN = (

    r"Page\s+\d+"

)

# ==========================
# Table of Contents
# ==========================

TOC_PATTERN = (

    r"(BAB|Chapter|Gambar|Figure|Tabel|Table).*?\.{3,}\s*\d+"

)

# ==========================
# OCR Noise
# ==========================

OCR_PATTERN = (

    r"[■□●◆▲▼►◄▪▫◦]+"

)

# ==========================
# Clean Text
# ==========================

def clean_document_text(text):

    # ----------------------
    # Remove Header
    # ----------------------

    for pattern in HEADER_PATTERNS:

        text = re.sub(
            pattern,
            "",
            text,
            flags=re.IGNORECASE
        )

    # ----------------------
    # Remove Footer
    # ----------------------

    for pattern in FOOTER_PATTERNS:

        text = re.sub(
            pattern,
            "",
            text,
            flags=re.IGNORECASE
        )

    # ----------------------
    # Remove Page Number
    # ----------------------

    text = re.sub(
        PAGE_PATTERN,
        "",
        text,
        flags=re.IGNORECASE
    )

    # ----------------------
    # Remove Table of Contents
    # ----------------------

    text = re.sub(
        TOC_PATTERN,
        "",
        text,
        flags=re.IGNORECASE
    )

    # ----------------------
    # Remove OCR Noise
    # ----------------------

    text = re.sub(
        OCR_PATTERN,
        "",
        text
    )

    # ----------------------
    # Normalize Spaces
    # ----------------------

    text = re.sub(
        r"\n{3,}",
        "\n\n",
        text
    )

    text = re.sub(
        r"[ \t]{2,}",
        " ",
        text
    )

    return text.strip()

# ==========================
# Remove Empty Pages
# ==========================

def remove_empty_pages(
    documents
):

    cleaned = []

    for doc in documents:

        content = clean_document_text(
            doc.page_content
        )

        if len(content) < 50:

            continue

        doc.page_content = content

        cleaned.append(
            doc
        )

    return cleaned