from flask import Flask, render_template, request
from pypdf import PdfReader
from ai_analyzer import analyze_resume_ai
import os

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

    reader = PdfReader(filepath)

    text = ""

    for page in reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted

    ai_response = analyze_resume_ai(text)

    return render_template(
        "result.html",
        analysis=ai_response
    )


if __name__ == "__main__":
    app.run(debug=True)