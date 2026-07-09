def get_completeness(sections):

    total = 4

    present = 0

    checklist = {}

    section_names = {

        "skills":"Skills",

        "experience":"Experience",

        "education":"Education",

        "projects":"Projects"

    }

    for key,value in section_names.items():

        if sections[key]:

            checklist[value]="✓"

            present +=1

        else:

            checklist[value]="✗"

    percentage = int(

        (present/total)*100
    )

    return {

        "checklist":checklist,

        "percentage":percentage
    }