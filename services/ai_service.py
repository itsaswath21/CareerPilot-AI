import ollama


def analyze_resume(text):

    prompt = f"""
You are an expert ATS Resume Reviewer.

Analyze the following resume.

Return your answer using Markdown.

Use these sections:

# ATS Score

# Strengths

# Weaknesses

# Missing Skills

# Suggested Projects

# Interview Questions

# Career Advice

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

    return response["message"]["content"]