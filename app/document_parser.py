import fitz  # PyMuPDF

async def extract_text(file):
    """
    Extracts text from a PDF or TXT UploadFile.
    Supports async Streamlit/FastAPI calls.
    """
    filename = file.filename.lower()

    try:
        content = await file.read()

        if filename.endswith(".pdf"):
            doc = fitz.open(stream=content, filetype="pdf")
            return "\n".join([page.get_text() for page in doc])

        elif filename.endswith(".txt"):
            return content.decode("utf-8")

        else:
            return "❌ Unsupported file type. Please upload a PDF or TXT file only."

    except Exception as e:
        return f"❌ Error reading file: {str(e)}"

