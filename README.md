# 🚀 CareerPilot AI

An AI-powered career assistant that analyzes resumes, calculates ATS scores, recommends jobs, and provides personalized career improvement guidance.



## 🌟 Features

### 📄 AI Resume Analysis

- Upload resume PDF
- Extract resume content automatically
- Analyze resume using local AI model
- Generate ATS compatibility score


### 🎯 ATS Dashboard

CareerPilot provides:

- Resume score
- Detected strengths
- Missing skills
- Recommended career roles
- AI improvement suggestions



### 🌍 Live Job Recommendations

Integrated with Adzuna API to provide:

- Real-time job openings
- Company information
- Job location
- Direct application links



### 🤖 AI Job Match

Compare your resume against a specific job.

Provides:

- Match percentage
- Matching skills
- Missing skills
- Personalized preparation advice



## 🛠 Tech Stack

### Frontend

- HTML
- CSS
- Bootstrap
- Jinja Templates


### Backend

- Python
- Flask


### AI

- Ollama
- Llama 3.2


### APIs

- Adzuna Jobs API



## 🏗 Project Architecture


```
CareerPilot-AI

├── app.py

├── services
│
├── ai_service.py
│
├── pdf_service.py
│
├── job_service.py
│
├── match_service.py
│
└── report_service.py


├── templates

├── static

└── README.md
```



## 🚀 How To Run


Clone repository


```bash
git clone <repo-link>
```


Install dependencies


```bash
pip install -r requirements.txt
```


Run application


```bash
python3 app.py
```


Open:


```
http://127.0.0.1:5000
```



## 👨‍💻 Developer

Built with ❤️ by Aswath Sreedhar
