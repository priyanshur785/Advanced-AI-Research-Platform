import cohere
from dotenv import load_dotenv
import os

# Load env vars
load_dotenv()
cohere_client = cohere.Client("bEsBenWWujjJxqeGzSoeI5Vi0XcJTcpNt1jvlXEr")

def summarize_text(content: str):
    """
    Summarizes the input document content in <=150 words using Cohere.
    """
    try:
        response = cohere_client.summarize(
            text=content[:3000],         # limit for API efficiency
            length='short',
            format='paragraph',
            temperature=0.3
        )
        return response.summary
    except Exception as e:
        return f"Error in summarization: {str(e)}"
