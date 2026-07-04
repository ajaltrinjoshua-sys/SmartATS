from flask import Flask, render_template, request
import os
from PyPDF2 import PdfReader

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["resume"]

    if file:

        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            file.filename
        )

        file.save(filepath)

        reader = PdfReader(filepath)

        resume_text = ""

        for page in reader.pages:
            resume_text += page.extract_text()

        # Keep line breaks
        resume_text = resume_text.replace("\n", "<br>")

        # Skills to detect
        skills = [
            "Python",
            "Java",
            "C++",
            "Machine Learning",
            "HTML",
            "CSS",
            "Flask"
        ]

        found_skills = []

        for skill in skills:
            if skill.lower() in resume_text.lower():
                found_skills.append(skill)

        return f"""
        Resume uploaded successfully! <br><br>

        File Name: {file.filename}<br><br>

        Resume Content:<br><br>

        {resume_text}<br><br>

        Detected Skills:<br>
        {", ".join(found_skills)}
        """

if __name__ == "__main__":
    app.run(debug=True)