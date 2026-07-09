import re


def extract_contact_info(text):

    contact = {

        "name": "Not Found",
        "email": "Not Found",
        "phone": "Not Found",
        "linkedin": "Not Found",
        "github": "Not Found"

    }


    # Name (first non-empty line)

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if len(line) > 2:

            contact["name"] = line.title()

            break


    # Email

    email = re.search(

        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",

        text

    )

    if email:

        contact["email"] = email.group()


    # Phone Number

    phone = re.search(

        r"(\+?\d[\d\s\-]{8,15})",

        text

    )

    if phone:

        contact["phone"] = phone.group().strip()


    # LinkedIn

    linkedin = re.search(

        r"(https?://)?(www\.)?linkedin\.com/[^\s]+",

        text

    )

    if linkedin:

        contact["linkedin"] = linkedin.group()


    # GitHub

    github = re.search(

        r"(https?://)?(www\.)?github\.com/[^\s]+",

        text

    )

    if github:

        contact["github"] = github.group()


    return contact