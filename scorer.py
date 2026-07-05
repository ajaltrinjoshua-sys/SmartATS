def calculate_score(
    found_skills,
    occupation_data
):

    must_have = occupation_data["must_have"]

    optional = occupation_data["optional"]

    total_possible = (
        len(must_have)*15
        +
        len(optional)*5
    )

    obtained = 0

    for skill in found_skills:

        if skill in must_have:

            obtained += 15

        elif skill in optional:

            obtained += 5


    final_score = (
        obtained/total_possible
    )*100

    return round(final_score)