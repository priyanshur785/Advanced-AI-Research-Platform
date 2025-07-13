import cohere
from dotenv import load_dotenv
import os

load_dotenv()
cohere_client = cohere.Client("bEsBenWWujjJxqeGzSoeI5Vi0XcJTcpNt1jvlXEr")

generated_questions = []

def generate_logic_questions(doc_text: str):
    """
    Generates 3 logic or comprehension-based questions using Cohere.
    """
    global generated_questions
    prompt = (
        "Based on the following document, generate 3 logic-based or comprehension-focused questions. "
        "Avoid yes/no or factual-only questions. Format as:\n\n"
        "1. ...\n2. ...\n3. ...\n\n"
        f"Document:\n{doc_text[:3000]}"
    )

    try:
        response = cohere_client.generate(
            model="command",
            prompt=prompt,
            temperature=0.5,
            max_tokens=300
        )
        raw = response.generations[0].text.strip()
        generated_questions = [
            line.split('. ', 1)[1] if '. ' in line else line
            for line in raw.splitlines()
            if line.strip() and line[0].isdigit()
        ]
        return generated_questions

    except Exception as e:
        return [f"Error generating questions: {str(e)}"]
