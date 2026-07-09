from flask import Flask, render_template, request
import os

from parser import extract_text
from matcher import find_skills
from matcher import get_occupation_data
from scorer import calculate_score
from suggestions import get_suggestions
from explain import get_breakdown
from analyzer import analyze_resume_sections
from strength import get_strength
from visualizer import get_skill_stats
from contact_extractor import extract_contact_info

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():

    return render_template(
        "index.html"
    )


@app.route(
    "/upload",
    methods=["POST"]
)
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

        resume_text, sections = extract_text(filepath)

        contact = extract_contact_info(resume_text)

        found_skills, skills = find_skills(

            resume_text,
            job_description,
            occupation
        )

        occupation_data = get_occupation_data(
            occupation
        )

        score = calculate_score(

            found_skills,
            occupation_data
        )

        strength = get_strength(
            score
        )

        stats = get_skill_stats(
            found_skills,
            skills
        )

        missing_skills = []

        for skill in skills:

            if skill not in found_skills:

                missing_skills.append(
                    skill
                )

        recommendations = get_suggestions(
            missing_skills
        )

        breakdown = get_breakdown(

            found_skills,
            occupation_data
        )

        analysis = analyze_resume_sections(
            sections
        )
        print(contact)
        print(sections["summary"])
        return render_template(

            "result.html",

            occupation=occupation,

            contact=contact,

            score=score,

            strength=strength,

            found_skills=found_skills,

            missing_skills=missing_skills,

            recommendations=recommendations,

            breakdown=breakdown,

            feedback=analysis["feedback"],

            completeness=analysis["completeness"],

            stats=stats,

            occupation_data=occupation_data

        )


if __name__ == "__main__":

    app.run(
        debug=True
    )