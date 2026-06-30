from flask import Flask, render_template, request
import markdown
import os

from services.pdf_service import extract_text_from_pdf
from services.ai_service import analyze_resume

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["resume"]

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)

    text = extract_text_from_pdf(filepath)

    analysis = analyze_resume(text)

    analysis = markdown.markdown(analysis)

    return render_template(
        "result.html",
        analysis=analysis
    )


if __name__ == "__main__":
    app.run(debug=True)