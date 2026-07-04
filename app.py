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
        
        # Score ccalculation based on the number of skills found
        total_skills = len(skills)
        matched_skills = len(found_skills)
        score = (matched_skills / total_skills) * 100 if total_skills > 0 else 0

        #List of missing skills
        missing_skills =[]
        for skill in skills:
            if skill not in found_skills:
                missing_skills.append(skill)

        #Return

        return f"""
        Resume uploaded successfully! <br><br>

        File Name: {file.filename}<br><br>

        Resume Content:<br><br>

        {resume_text}<br><br>

        Detected Skills:<br>
        {", ".join(found_skills)}<br><br>

        Resume Score:<br>
        {score:.0f}/100<br><br>

        Suggestions for Improvement:<br>
        Add the following skills to your resume to improve your score: {", ".join(missing_skills)}<br><br>
        """

if __name__ == "__main__":
    app.run(debug=True)