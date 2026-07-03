import ollama
import json
import re


def calculate_match(resume_analysis, job):

    prompt = f"""

You are an AI career advisor.

Compare this resume profile:

{resume_analysis}


With this job:

{job}


Return ONLY JSON.

Format:

{{
    "match_score": 80,
    "matched_skills": [
        "Python"
    ],
    "missing_skills": [
        "Docker"
    ],
    "recommendation": "Advice here"
}}

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


    except:


        return {

            "match_score":0,

            "matched_skills":[],

            "missing_skills":[],

            "recommendation":
            "Could not calculate match"

        }