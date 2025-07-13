import streamlit as st
import requests
import time
from streamlit_lottie import st_lottie
import json

# Page configuration
st.set_page_config(
    page_title="EZ Smart Assistant", 
    layout="wide",
    page_icon="🧠",
    initial_sidebar_state="collapsed"
)

# Custom CSS for professional styling and animations
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    .main {
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom Header Animation */
    .animated-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        animation: slideInDown 0.8s ease-out;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
    }
    
    .animated-header h1 {
        color: white;
        text-align: center;
        font-weight: 700;
        font-size: 2.5rem;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .animated-header p {
        color: rgba(255,255,255,0.9);
        text-align: center;
        font-size: 1.1rem;
        margin-top: 0.5rem;
        font-weight: 300;
    }
    
    /* Animations */
    @keyframes slideInDown {
        from {
            transform: translateY(-100px);
            opacity: 0;
        }
        to {
            transform: translateY(0);
            opacity: 1;
        }
    }
    
    @keyframes fadeInUp {
        from {
            transform: translateY(30px);
            opacity: 0;
        }
        to {
            transform: translateY(0);
            opacity: 1;
        }
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    /* Card Styles */
    .feature-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        margin: 1rem 0;
        border-left: 4px solid #667eea;
        animation: fadeInUp 0.6s ease-out;
        transition: all 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(0,0,0,0.15);
    }
    
    .feature-card h3 {
        color: #2d3748;
        font-weight: 600;
        margin-bottom: 1rem;
        font-size: 1.3rem;
    }
    
    /* Upload Area */
    .upload-area {
        border: 2px dashed #667eea;
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.05) 0%, rgba(118, 75, 162, 0.05) 100%);
        margin: 1rem 0;
        transition: all 0.3s ease;
    }
    
    .upload-area:hover {
        border-color: #764ba2;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
    }
    
    /* Success/Error Messages */
    .success-message {
        background: linear-gradient(135deg, #48bb78 0%, #38a169 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        animation: pulse 0.5s ease-in-out;
    }
    
    .error-message {
        background: linear-gradient(135deg, #f56565 0%, #e53e3e 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        animation: pulse 0.5s ease-in-out;
    }
    
    /* Button Styles */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
    }
    
    /* Input Styles */
    .stTextInput > div > div > input {
        border-radius: 10px;
        border: 2px solid #e2e8f0;
        padding: 0.75rem;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Progress Bar */
    .stProgress > div > div > div > div {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Expander Styles */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        border-radius: 10px;
    }
    
    /* Loading Animation */
    .loading-container {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 2rem;
    }
    
    .loading-spinner {
        width: 40px;
        height: 40px;
        border: 4px solid #f3f3f3;
        border-top: 4px solid #667eea;
        border-radius: 50%;
        animation: spin 1s linear infinite;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    /* Section Dividers */
    .section-divider {
        height: 2px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        margin: 2rem 0;
        border-radius: 1px;
    }
    
    /* Stats Cards */
    .stats-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        margin: 0.5rem;
        animation: fadeInUp 0.8s ease-out;
    }
    
    .stats-number {
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .stats-label {
        font-size: 0.9rem;
        opacity: 0.9;
    }
    .st-emotion-cache-seewz2 {
        font-family: "Source Sans Pro", sans-serif;
        font-size: 1rem;
        margin-bottom: -1rem;
        color: rgb(163, 168, 184);
    }        
</style>
""", unsafe_allow_html=True)

# Animated Header
st.markdown("""
<div class="animated-header">
    <h1>🧠 EZ Smart Assistant</h1>
    <p>Advanced Research Summarization & Intelligence Platform</p>
</div>
""", unsafe_allow_html=True)

# Initialize session state
if "doc_text" not in st.session_state:
    st.session_state.doc_text = ""
if "challenge_questions" not in st.session_state:
    st.session_state.challenge_questions = []
if "upload_success" not in st.session_state:
    st.session_state.upload_success = False

# Create columns for layout
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Upload Section with enhanced styling
    st.markdown("""
    <div class="feature-card">
        <h3>📄 Document Upload</h3>
        <div class="upload-area">
            <h4>Drop your research paper here</h4>
            <p>Supported formats: PDF, TXT</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("", type=["pdf", "txt"], label_visibility="collapsed")

    if uploaded_file:
        # Custom loading animation
        with st.container():
            st.markdown('<div class="loading-container"><div class="loading-spinner"></div></div>', unsafe_allow_html=True)
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            try:
                # Simulate processing steps with progress
                for i in range(100):
                    progress_bar.progress(i + 1)
                    if i < 30:
                        status_text.text("📤 Uploading document...")
                    elif i < 60:
                        status_text.text("🔍 Analyzing content...")
                    elif i < 90:
                        status_text.text("📝 Generating summary...")
                    else:
                        status_text.text("✅ Processing complete!")
                    time.sleep(0.01)
                
                files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
                response = requests.post("http://localhost:8000/upload", files=files, timeout=30)
                response.raise_for_status()
                
                result = response.json()
                st.session_state.doc_text = result["text"]
                st.session_state.upload_success = True
                
                # Clear progress indicators
                progress_bar.empty()
                status_text.empty()
                
                # Success message
                st.markdown("""
                <div class="success-message">
                    ✅ Document successfully processed and analyzed!
                </div>
                """, unsafe_allow_html=True)
                
                # Summary Section
                st.markdown("""
                <div class="feature-card">
                    <h3>📄 Intelligent Summary</h3>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, rgba(102, 126, 234, 0.05) 0%, rgba(118, 75, 162, 0.05) 100%); 
                           padding: 1.5rem; border-radius: 10px; border-left: 4px solid #667eea;">
                    {result["summary"]}
                </div>
                """, unsafe_allow_html=True)
                
            except Exception as e:
                progress_bar.empty()
                status_text.empty()
                st.markdown(f"""
                <div class="error-message">
                    ❌ Upload failed: {str(e)}
                </div>
                """, unsafe_allow_html=True)
                st.stop()

    # Section Divider
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    # Q&A Section
    if st.session_state.upload_success:
        st.markdown("""
        <div class="feature-card">
            <h3>🗨️ Interactive Q&A</h3>
            <p>Ask any question about your document and get intelligent answers with context.</p>
        </div>
        """, unsafe_allow_html=True)
        
        question = st.text_input("💭 What would you like to know?", placeholder="Enter your question here...")
        
        if question:
            with st.spinner("🤔 Analyzing your question..."):
                try:
                    res = requests.get("http://localhost:8000/ask", params={"question": question}, timeout=30)
                    res.raise_for_status()
                    qa = res.json()

                    # Answer Section
                    st.markdown("### ✅ Answer")
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, rgba(72, 187, 120, 0.1) 0%, rgba(56, 161, 105, 0.1) 100%); 
                               padding: 1.5rem; border-radius: 10px; border-left: 4px solid #48bb78; margin: 1rem 0;">
                        {qa["answer"]}
                    </div>
                    """, unsafe_allow_html=True)

                    # Context Section
                    st.markdown("### 📌 Supporting Evidence")
                    for i, context in enumerate(qa["justification"], start=1):
                        with st.expander(f"📄 Reference {i}", expanded=False):
                            st.markdown(f"""
                            <div style="background: #f7fafc; padding: 1rem; border-radius: 8px; font-style: italic;">
                                {context}
                            </div>
                            """, unsafe_allow_html=True)
                            
                except Exception as e:
                    st.markdown(f"""
                    <div class="error-message">
                        ❌ Failed to get answer: {str(e)}
                    </div>
                    """, unsafe_allow_html=True)

        # Section Divider
        st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

        # Challenge Section
        st.markdown("""
        <div class="feature-card">
            <h3>🧠 Intelligence Challenge</h3>
            <p>Test your understanding with AI-generated logic questions based on your document.</p>
        </div>
        """, unsafe_allow_html=True)

        col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
        with col_btn2:
            if st.button("🔄 Generate Challenge Questions", use_container_width=True):
                with st.spinner("🎯 Creating personalized questions..."):
                    try:
                        res = requests.post("http://localhost:8000/challenge/generate", 
                                          json={"doc_text": st.session_state.doc_text}, timeout=30)
                        res.raise_for_status()
                        st.session_state.challenge_questions = res.json()["questions"]
                        
                        st.markdown("""
                        <div class="success-message">
                            🎉 Challenge questions generated successfully!
                        </div>
                        """, unsafe_allow_html=True)
                        
                    except Exception as e:
                        st.markdown(f"""
                        <div class="error-message">
                            ❌ Question generation failed: {str(e)}
                        </div>
                        """, unsafe_allow_html=True)

        if st.session_state.challenge_questions:
            st.markdown("### 📝 Challenge Questions")
            
            with st.form("challenge_form"):
                answers = []
                for idx, question in enumerate(st.session_state.challenge_questions):
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, rgba(102, 126, 234, 0.05) 0%, rgba(118, 75, 162, 0.05) 100%); 
                               padding: 1.5rem; border-radius: 10px; margin: 1rem 0; border-left: 4px solid #667eea;">
                        <strong>Question {idx+1}:</strong><br>
                        {question}
                    </div>
                    """, unsafe_allow_html=True)
                    
                    answer = st.text_area(f"Your Answer {idx+1}", 
                                        key=f"answer_{idx}", 
                                        placeholder="Type your detailed answer here...",
                                        height=100)
                    answers.append(answer)

                col_submit1, col_submit2, col_submit3 = st.columns([1, 2, 1])
                with col_submit2:
                    submitted = st.form_submit_button("📤 Submit for Evaluation", use_container_width=True)
                    
                if submitted:
                    with st.spinner("🔍 Evaluating your responses..."):
                        eval_payload = {
                            "answers": answers,
                            "questions": st.session_state.challenge_questions,
                            "doc_text": st.session_state.doc_text
                        }
                        try:
                            res = requests.post("http://localhost:8000/challenge/evaluate", 
                                              json=eval_payload, timeout=60)
                            res.raise_for_status()
                            feedback = res.json()["feedback"]

                            st.markdown("## 🧾 Detailed Evaluation")
                            for i, fb in enumerate(feedback):
                                with st.expander(f"📊 Feedback for Question {i+1}", expanded=True):
                                    st.markdown(f"""
                                    <div style="background: #f7fafc; padding: 1.5rem; border-radius: 10px; 
                                               border-left: 4px solid #667eea;">
                                        {fb}
                                    </div>
                                    """, unsafe_allow_html=True)
                                    
                        except Exception as e:
                            st.markdown(f"""
                            <div class="error-message">
                                ❌ Evaluation failed: {str(e)}
                            </div>
                            """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; padding: 2rem; color: #718096; margin-top: 3rem;">
    <p>Powered by Priyanshu Rai | Advanced AI Research Platform</p>
</div>
""", unsafe_allow_html=True)
