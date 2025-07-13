from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os

from app.document_parser import extract_text
from app.summarizer import summarize_text
from app.qa_engine import index_document, answer_question
from app.logic_qa_generator import generate_logic_questions
from app.evaluator import evaluate_user_answers

load_dotenv()

app = FastAPI(
    title="EZ Smart Assistant API",
    description="Backend for summarization, Q&A, and evaluation of research documents.",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        raw_text = await extract_text(file)
        index_document(raw_text)
        summary = summarize_text(raw_text)
        return {"summary": summary, "text": raw_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload processing failed: {str(e)}")

@app.get("/ask")
def ask_question(question: str):
    try:
        answer, context = answer_question(question)
        return {"answer": answer, "justification": context}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Q&A failed: {str(e)}")

class ChallengeInput(BaseModel):
    doc_text: str

@app.post("/challenge/generate")
def get_challenge_questions(request: ChallengeInput):
    try:
        questions = generate_logic_questions(request.doc_text)
        return {"questions": questions}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Challenge generation failed: {str(e)}")

class EvaluatePayload(BaseModel):
    answers: list
    questions: list
    doc_text: str

@app.post("/challenge/evaluate")
def evaluate_answers(payload: EvaluatePayload):
    try:
        feedback = evaluate_user_answers(payload.answers, payload.questions, payload.doc_text)
        return {"feedback": feedback}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Evaluation failed: {str(e)}")
