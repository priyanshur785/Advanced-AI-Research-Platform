from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import cohere
import re
import os
from dotenv import load_dotenv

load_dotenv()
cohere_client = cohere.Client("bEsBenWWujjJxqeGzSoeI5Vi0XcJTcpNt1jvlXEr")

model = SentenceTransformer("all-MiniLM-L6-v2")

text_chunks = []
index = None

def split_text(text, chunk_size=200):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks, current = [], ""
    for sentence in sentences:
        if len(current.split()) + len(sentence.split()) < chunk_size:
            current += sentence + " "
        else:
            chunks.append(current.strip())
            current = sentence + " "
    if current:
        chunks.append(current.strip())
    return chunks

def index_document(text):
    global text_chunks, index
    text_chunks = split_text(text)
    embeddings = model.encode(text_chunks)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))

def get_context(query, top_k=3):
    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding), top_k)
    return [text_chunks[i] for i in I[0]]

def answer_question(question):
    context = get_context(question)
    prompt = (
        f"Use the following excerpts from a document to answer the question:\n\n"
        f"{'-'*20}\n" +
        "\n---\n".join(context) +
        f"\n{'-'*20}\nQuestion: {question}\nAnswer:"
    )

    try:
        response = cohere_client.generate(
            model="command",
            prompt=prompt,
            temperature=0.3,
            max_tokens=300
        )
        return response.generations[0].text.strip(), context
    except Exception as e:
        return f"Error from Cohere: {str(e)}", context
