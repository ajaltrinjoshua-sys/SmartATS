def analyze_resume_sections(sections):

    feedback = []

    checklist = {}

    required_sections = [
        "skills",
        "experience",
        "education",
        "projects"
    ]

    found_count = 0

    for section in required_sections:

        content = sections.get(section, "").strip()

        if content:

            found_count += 1

            checklist[section.capitalize()] = "✓"

            if section == "skills":
                feedback.append(
                    "✓ Skills section detected."
                )

            elif section == "experience":
                feedback.append(
                    "✓ Work experience detected."
                )

            elif section == "education":
                feedback.append(
                    "✓ Education section detected."
                )

            elif section == "projects":
                feedback.append(
                    "✓ Projects section detected."
                )

        else:

            checklist[section.capitalize()] = "✗"

            if section == "skills":
                feedback.append(
                    "⚠ Add a Skills section."
                )

            elif section == "experience":
                feedback.append(
                    "⚠ Add Internship or Work Experience."
                )

            elif section == "education":
                feedback.append(
                    "⚠ Add Education details."
                )

            elif section == "projects":
                feedback.append(
                    "⚠ Add Projects with technologies used."
                )

    # ---------- Extra Checks ----------

    if sections.get("certifications", "").strip():

        feedback.append(
            "✓ Certifications found."
        )

    else:

        feedback.append(
            "⚠ Consider adding Certifications."
        )

    if sections.get("achievements", "").strip():

        feedback.append(
            "✓ Achievements found."
        )

    else:

        feedback.append(
            "⚠ Consider adding Achievements."
        )

    # ---------- Resume Completeness ----------

    percentage = round(
        (found_count / len(required_sections)) * 100
    )

    return {

        "feedback": feedback,

        "completeness": {

            "percentage": percentage,

            "checklist": checklist

        }

    }