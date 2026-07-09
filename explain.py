def get_breakdown(

    found_skills,
    occupation_data
):

    must_have = occupation_data["must_have"]

    optional = occupation_data["optional"]

    breakdown = []

    for skill in found_skills:

        if skill in must_have:

            breakdown.append(
                f"{skill} (+15)"
            )

        elif skill in optional:

            breakdown.append(
                f"{skill} (+5)"
            )

    return breakdown