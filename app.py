from flask import Flask, render_template, request
import os
from PyPDF2 import PdfReader
from docx import Document

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["resume"]

    occupation = request.form["occupation"]

    if file:

        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            file.filename
        )

        file.save(filepath)

        resume_text = ""

        # PDF extraction
        if file.filename.endswith(".pdf"):

            reader = PdfReader(filepath)

            for page in reader.pages:

                extracted = page.extract_text()

                if extracted:
                    resume_text += extracted

        # DOCX extraction
        elif file.filename.endswith(".docx"):

            doc = Document(filepath)

            for paragraph in doc.paragraphs:

                resume_text += paragraph.text + "\n"

        resume_text = resume_text.replace(
            "\n",
            "<br>"
        )

        job_skills = {

            "Full Stack Developer":
            ["HTML","CSS","JavaScript","Python","Flask","SQL"],

            "Cloud Engineer":
            ["AWS","Linux","Docker","Kubernetes","Python"],

            "Cyber Security Analyst":
            ["Networking","Linux","Python","Wireshark"],

            "Data Scientist":
            ["Python","Machine Learning","Pandas","SQL"]
        }

        skills = job_skills[occupation]

        found_skills=[]

        for skill in skills:

            if skill.lower() in resume_text.lower():

                found_skills.append(skill)

        total_skills=len(skills)

        matched_skills=len(found_skills)

        score=(matched_skills/total_skills)*100

        missing_skills=[]

        for skill in skills:

            if skill not in found_skills:

                missing_skills.append(skill)

        return f"""
        Resume uploaded successfully!<br><br>

        Occupation:
        {occupation}<br><br>

        File Name:
        {file.filename}<br><br>

        Resume Content:<br><br>

        {resume_text}<br><br>

        Detected Skills:<br>

        {", ".join(found_skills)}<br><br>

        Resume Score:<br>

        {score:.0f}/100<br><br>

        Suggestions:<br>

        Add these skills:
        {", ".join(missing_skills)}
        """

if __name__=="__main__":
    app.run(debug=True)