from flask import Flask, render_template, request, send_file
import os

from services.pdf_service import extract_text_from_pdf
from services.ai_service import analyze_resume
from services.report_service import create_report

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
REPORT_FOLDER = "reports"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["REPORT_FOLDER"] = REPORT_FOLDER

latest_analysis = {}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/upload", methods=["POST"])
def upload():

    global latest_analysis

    file = request.files["resume"]

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)

    # Extract text from PDF
    text = extract_text_from_pdf(filepath)

    # AI Analysis (returns JSON/dictionary)
    analysis = analyze_resume(text)

    latest_analysis = analysis

    return render_template(
        "dashboard.html",
        analysis=analysis
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