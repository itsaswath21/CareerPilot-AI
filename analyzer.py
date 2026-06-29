def analyze_resume(text):

    skills = [
        "Python",
        "Java",
        "C",
        "C++",
        "SQL",
        "HTML",
        "CSS",
        "JavaScript",
        "Flask",
        "Git",
        "Machine Learning",
        "AI",
        "Data Structures",
        "Docker",
        "Linux",
        "React"
    ]

    found_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    score = min(len(found_skills) * 10, 100)

    word_count = len(text.split())

    return {
        "score": score,
        "skills": found_skills,
        "word_count": word_count,
        "characters": len(text),
        "preview": text[:500]
    }