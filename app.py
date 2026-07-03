from flask import Flask, render_template, request, send_file
import os

from services.pdf_service import extract_text_from_pdf
from services.ai_service import analyze_resume
from services.report_service import create_report
from services.job_service import recommend_jobs
from services.match_service import calculate_match


app = Flask(__name__)


UPLOAD_FOLDER = "uploads"
REPORT_FOLDER = "reports"


app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["REPORT_FOLDER"] = REPORT_FOLDER


latest_analysis = {}
latest_jobs = []
latest_match = {}



@app.route("/")
def home():

    return render_template(
        "home.html"
    )



@app.route("/upload", methods=["POST"])
def upload():

    global latest_analysis
    global latest_jobs


    file = request.files["resume"]


    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )


    file.save(filepath)


    text = extract_text_from_pdf(filepath)


    analysis = analyze_resume(text)


    latest_analysis = analysis


    skills = analysis.get(
        "strengths",
        []
    )


    latest_jobs = recommend_jobs(
        skills
    )


    return render_template(

        "dashboard.html",

        analysis=analysis,

        jobs=latest_jobs

    )




@app.route("/match/<int:index>")
def match_job(index):

    global latest_match


    selected_job = latest_jobs[index]


    latest_match = calculate_match(

        latest_analysis,

        selected_job

    )


    return render_template(

        "match.html",

        match=latest_match,

        job=selected_job

    )





@app.route("/download")
def download():


    filename = os.path.join(

        app.config["REPORT_FOLDER"],

        "CareerPilot_Report.pdf"

    )


    create_report(

        str(latest_analysis),

        filename

    )


    return send_file(

        filename,

        as_attachment=True

    )





if __name__ == "__main__":

    app.run(debug=True)