def get_skill_stats(

    found_skills,
    all_skills
):

    matched = len(
        found_skills
    )

    total = len(
        all_skills
    )

    missing = (
        total - matched
    )

    percentage = int(

        (matched/total)*100

    )

    filled = int(
        percentage/10
    )

    bar = (

        "█"*filled
        +
        "░"*(10-filled)

    )

    return {

        "matched":matched,

        "missing":missing,

        "bar":bar,

        "percentage":percentage
    }