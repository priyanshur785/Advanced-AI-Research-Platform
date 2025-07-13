import cohere
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
cohere_client = cohere.Client("bEsBenWWujjJxqeGzSoeI5Vi0XcJTcpNt1jvlXEr")

def evaluate_user_answers(user_answers: list, questions: list, context_text: str):
    """
    Evaluates a list of user's answers (one per question) against the corresponding questions and document context.
    For any question with an empty answer, it outputs a default "No answer provided" feedback.
    Returns a list of feedback responses, one for each answer.
    """
    results = []

    # Validation: Ensure both lists contain exactly 3 items
    if len(user_answers) != 3 or len(questions) != 3:
        return ["❌ Missing questions or answers. Expected exactly 3 of each."]

    for i in range(3):
        question = questions[i]
        user_ans = user_answers[i].strip()  # Remove extra whitespace

        # If no answer is provided, set a default response
        if not user_ans:
            results.append("No answer provided for this question.")
            continue

        prompt = (
            f"Question: {question}\n"
            f"User's Answer: {user_ans}\n"
            f"Based on this document (first 3000 chars):\n{context_text[:3000]}\n\n"
            f"Evaluate the user's answer. Respond with:\n"
            f"- Correctness (1–10 scale)\n"
            f"- Justification (with quotes if possible)\n"
            f"- Suggested improvement (if needed)"
        )

        try:
            response = cohere_client.generate(
                model="command",
                prompt=prompt,
                temperature=0.4,
                max_tokens=300
            )
            feedback = response.generations[0].text.strip()
            results.append(feedback)
        except Exception as e:
            results.append(f"❌ Error evaluating Q{i+1}: {str(e)}")

    return results
