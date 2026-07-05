import json


def get_skills(occupation):

    with open(
        "data/skills.json",
        "r"
    ) as file:

        data = json.load(file)

    return data[occupation]


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

    all_skills = must_have + optional

    found_skills = []

    for skill in all_skills:

        if (
            skill.lower() in resume_text
            and
            skill.lower() in job_description.lower()
        ):

            found_skills.append(skill)

    return found_skills, all_skills

def get_occupation_data(
    occupation
):

    return get_skills(
        occupation
    )