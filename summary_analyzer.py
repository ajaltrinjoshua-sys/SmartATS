def analyze_summary(summary, occupation):

    result = {

        "score": 0,
        "rating": "",
        "checks": [],
        "suggestions": []

    }

    summary = summary.strip()

    if summary == "":

        result["checks"].append("❌ No professional summary found.")

        result["suggestions"].append(
            "Add a professional summary at the beginning of your resume."
        )

        result["rating"] = "Poor"

        return result

    score = 0

    # Length Check

    words = summary.split()

    if len(words) >= 40:

        score += 25

        result["checks"].append(
            "✅ Good summary length."
        )

    elif len(words) >= 20:

        score += 15

        result["checks"].append(
            "⚠ Summary is acceptable but could be longer."
        )

        result["suggestions"].append(
            "Expand your summary to around 40-60 words."
        )

    else:

        result["checks"].append(
            "❌ Summary is too short."
        )

        result["suggestions"].append(
            "Write at least 40 words describing yourself."
        )

    # Occupation Mention

    if occupation.lower() in summary.lower():

        score += 25

        result["checks"].append(
            "✅ Occupation mentioned."
        )

    else:

        result["suggestions"].append(
            f"Mention your target role ({occupation}) in the summary."
        )

    # Technology Check

    technologies = [

        "python",
        "java",
        "c++",
        "sql",
        "flask",
        "django",
        "machine learning",
        "deep learning",
        "html",
        "css",
        "javascript",
        "react",
        "node",
        "mongodb"

    ]

    found = 0

    for tech in technologies:

        if tech in summary.lower():

            found += 1

    if found >= 3:

        score += 25

        result["checks"].append(
            "✅ Technologies mentioned."
        )

    else:

        result["suggestions"].append(
            "Mention your core technical skills."
        )

    # Career Objective

    keywords = [

        "seeking",
        "looking",
        "passionate",
        "interested",
        "aim",
        "objective",
        "career"

    ]

    found_goal = False

    for word in keywords:

        if word in summary.lower():

            found_goal = True

            break

    if found_goal:

        score += 25

        result["checks"].append(
            "✅ Career objective present."
        )

    else:

        result["suggestions"].append(
            "Mention your career objective."
        )

    result["score"] = score

    if score >= 80:

        result["rating"] = "Excellent"

    elif score >= 60:

        result["rating"] = "Good"

    elif score >= 40:

        result["rating"] = "Average"

    else:

        result["rating"] = "Poor"

    return result