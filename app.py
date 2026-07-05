from flask import Flask, render_template, request
import os
from parser import extract_text
from matcher import find_skills
from scorer import calculate_score
from matcher import get_occupation_data

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

    job_description = request.form["job_description"]

    if file:

        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            file.filename
        )

        file.save(filepath)

        resume_text = ""

        resume_text, sections = extract_text(filepath)

        # Occupation skills database
        found_skills, skills = find_skills(
            resume_text,
            job_description,
            occupation
)
        print("Found Skills:", found_skills)

        occupation_data = get_occupation_data(
             occupation
)

        score = calculate_score(
            found_skills,
            occupation_data
)

        missing_skills = []

        for skill in skills:

            if skill not in found_skills:

                missing_skills.append(skill)

        return render_template(

            "result.html",

            occupation=occupation,

            score=round(score),

            found_skills=found_skills,

            missing_skills=missing_skills
        )


if __name__=="__main__":
    app.run(debug=True)