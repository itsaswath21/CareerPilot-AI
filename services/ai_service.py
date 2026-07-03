import ollama
import json
import re


def analyze_resume(text):

    print("🧠 Starting resume AI analysis...")

    prompt = f"""

You are an ATS Resume Analyzer.

Analyze this resume:

{text}


Return ONLY JSON.

No explanation.
No markdown.

Use this exact format:

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
    "career_advice": "Advice here"
}}

"""


    response = ollama.chat(

        model="llama3.2",

        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]

    )


    print("✅ Resume AI replied")


    content = response["message"]["content"]


    content = content.replace(
        "```json",
        ""
    )

    content = content.replace(
        "```",
        ""
    )

    content = content.strip()


    match = re.search(
        r"\{.*\}",
        content,
        re.DOTALL
    )


    if match:

        content = match.group()


    try:

        return json.loads(content)


    except Exception as e:


        print("JSON ERROR:", e)

        print(content)


        return {

            "ats_score":50,

            "strengths":[
                "Unable to detect"
            ],

            "missing_skills":[
                "Unable to detect"
            ],

            "recommended_roles":[
                "Try again"
            ],

            "career_advice":
            "AI response format issue. Please analyze again."

        }