import ollama

def analyze_resume_ai(resume_text):

    prompt = f"""
You are an expert ATS Resume Reviewer.

Analyze the resume below.

Return your answer using Markdown headings and bullet points.

Use exactly these sections:

# ATS Score

# Strengths

# Weaknesses

# Missing Skills

# Suggested Projects

# Interview Questions

# Career Advice

Resume:

{resume_text}
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

    return response["message"]["content"]