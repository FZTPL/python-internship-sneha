from google import genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(
    api_key=GEMINI_API_KEY
)

def generate_questions(role: str,difficulty: str,num_questions: int) -> list[str]:
    prompt = f"""
    Generate {num_questions} interview questions
    for a {role} position.
    Difficulty: {difficulty}
    Return only the questions.
    One question per line.New questions should start from new line.
    Do not number the questions.
    """
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    questions_text = response.text
    questions = questions_text.split("\n")
    cleaned_questions = []
    for question in questions:
        question = question.strip()
        if question:
            cleaned_questions.append(question)
    return cleaned_questions

def evaluate_answer(question: str, answer: str):
    prompt = f"""
You are an expert technical interviewer.

Evaluate the user's answer.

Question: {question}
Answer: {answer}

Return ONLY valid JSON in this format:
{
  "score": 0-100,
  "feedback": "short and clear feedback"
}

Rules:
- No extra text
- Only valid JSON
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    data = json.loads(response.text)

    score = data["score"]
    feedback = data["feedback"]

    return score, feedback


def generate_ai_summary(
    role: str,
    difficulty: str,
    total_questions: int,
    answered_questions: int,
    average_score: float,
    feedback_text: str
):
    prompt = f"""
You are an expert technical interviewer.
Based on the interview results below, generate a concise overall evaluation.
Role: {role}
Difficulty: {difficulty}
Total Questions: {total_questions}
Answered Questions: {answered_questions}
Average Score: {average_score}
Question Feedbacks:
{feedback_text}
Write:
1. Overall performance summary
2. Key strengths
3. Areas for improvement
Keep the response under 150 words.
"""
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

