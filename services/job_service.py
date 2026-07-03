import os
import requests
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")


def recommend_jobs(skills):

    query = " ".join(skills[:3]) if skills else "Python"

    url = (
        f"https://api.adzuna.com/v1/api/jobs/in/search/1"
        f"?app_id={APP_ID}"
        f"&app_key={APP_KEY}"
        f"&results_per_page=5"
        f"&what={query}"
    )

    try:
        response = requests.get(url, timeout=10)

        

        if response.status_code != 200:
            return []

        data = response.json()

        jobs = []

        for job in data.get("results", []):

            jobs.append({
                "title": job.get("title", "Unknown"),
                "company": job.get("company", {}).get("display_name", "Unknown"),
                "location": job.get("location", {}).get("display_name", "Unknown"),
                "salary": job.get("salary_min", "Not Available"),
                "url": job.get("redirect_url", "#")
            })

        return jobs

    except Exception as e:
        print("Error:", e)
        return []