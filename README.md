# 🤖 Smart Research Assistant

[![Streamlit App](https://img.shields.io/badge/Built%20With-Streamlit-ff4b4b?logo=streamlit)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)

A smart assistant built with **Python** and **Streamlit** to assist researchers by:
- 📄 Summarizing uploaded documents
- ❓ Generating logic-based Q&A
- 🧠 Evaluating user answers with content logic

---

## 🚀 Features

- 📝 **Document Summarization**  
  Extracts key ideas from uploaded PDFs or text documents using LLMs.

- 🤔 **Logic-Based QA Generation**  
  Automatically generates intelligent, context-aware questions from the document summary.

- ✅ **Answer Evaluation**  
  Compares user responses with the source content to evaluate logic and accuracy.

- 🌐 **Interactive Web UI**  
  Clean and responsive Streamlit interface for seamless interaction.

---

## 🗂️ Project Structure

```bash
EZ project/
├── app/
│ ├── main.py # Orchestrates functionality
│ ├── summarizer.py # Summarizes text
│ ├── qa_engine.py # Extracts Q&A
│ ├── logic_qa_generator.py # Logic-based question generator
│ ├── evaluator.py # Evaluates answer quality
│ ├── document_parser.py # Cleans and extracts text
│ └── init.py
├── frontend/
│ └── streamlit_app.py # Streamlit web interface
├── requirements.txt # Required packages
└── README.md # Project documentation
```

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/your-username/smart-research-assistant.git
cd smart-research-assistant

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## ▶️ Run the App
```bash
Backend: uvicorn app.main:app --reload

Frontend: streamlit run frontend/streamlit_app.py
```

## 🔐 API Key Setup

```bash
cohere_client = your_key_here
```

## 🧭 How It Works
Upload Document → PDF or .txt is parsed and cleaned.

Summarize → summarizer.py uses LLMs to generate summaries.

Generate QA → logic_qa_generator.py creates logical questions.

Evaluate → evaluator.py uses embeddings to check answer correctness.

## 📸 Demo!
[![Screenshot-2025-07-13-231745.png](https://i.postimg.cc/PJRLN2wv/Screenshot-2025-07-13-231745.png)](https://postimg.cc/JHj723KR)

 Screenshot




## 📬 Contact
For questions or suggestions, feel free to contact:
📧 priyanshur785@gmail.com

