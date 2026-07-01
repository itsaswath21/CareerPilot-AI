import ollama
import json
import re


def analyze_resume(text):

    prompt = f"""
You are an ATS Resume Analyzer.

Analyze the following resume.

Return ONLY valid JSON.

Do NOT include explanations.
Do NOT include markdown.
Do NOT wrap the JSON inside ```.

Return EXACTLY this structure:

{{
    "ats_score": 85,
    "strengths": [
        "Python",
        "Flask"
    ],
    "missing_skills": [
        "Docker",
        "AWS"
    ],
    "recommended_roles": [
        "Backend Developer",
        "Software Engineer"
    ],
    "career_advice": "Your advice here."
}}

Resume:

{text}
"""

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response["message"]["content"]

    # Remove markdown if present
    content = content.replace("```json", "")
    content = content.replace("```", "")
    content = content.strip()

    # Extract only the JSON part
    match = re.search(r"\{.*\}", content, re.DOTALL)

    if match:
        content = match.group()

    try:
        return json.loads(content)

    except Exception:

        print("\n===== OLLAMA RESPONSE =====")
        print(content)
        print("===========================\n")

        return {
            "ats_score": 0,
            "strengths": [],
            "missing_skills": [],
            "recommended_roles": [],
            "career_advice": "AI could not analyze this resume."
        }