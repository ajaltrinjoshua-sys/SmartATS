import json
from rapidfuzz import fuzz


SYNONYMS = {

    "Machine Learning":["ML"],

    "JavaScript":["JS"],

    "Artificial Intelligence":["AI"],

    "Node.js":["Node"],

    "TensorFlow":["TF"],

    "User Interface":["UI"],

    "User Experience":["UX"]

}


def get_skills(occupation):

    with open(
        "data/skills.json",
        "r"
    ) as file:

        data = json.load(file)

    return data[occupation]


def fuzzy_match(skill, text):

    similarity = fuzz.partial_ratio(
        skill.lower(),
        text.lower()
    )

    return similarity > 80


def synonym_match(
    skill,
    text
):

    if skill in SYNONYMS:

        for synonym in SYNONYMS[skill]:

            if synonym.lower() in text.lower():

                return True

    return False


def find_skills(

    resume_text,
    job_description,
    occupation
):

    data = get_skills(
        occupation
    )

    must_have = data["must_have"]

    optional = data["optional"]

    all_skills = (
        must_have +
        optional
    )

    found_skills = []

    for skill in all_skills:

        resume_found = (

            fuzzy_match(
                skill,
                resume_text
            )

            or

            synonym_match(
                skill,
                resume_text
            )

        )

        jd_found = (

            fuzzy_match(
                skill,
                job_description
            )

            or

            synonym_match(
                skill,
                job_description
            )

        )

        if resume_found and jd_found:

            found_skills.append(
                skill
            )

    print(
        "Found Skills:",
        found_skills
    )

    return found_skills, all_skills


def get_occupation_data(
    occupation
):

    return get_skills(
        occupation
    )