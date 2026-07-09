def get_suggestions(

    missing_skills
):

    suggestions = {

        # Full Stack Developer
        "HTML":
        "Build responsive web pages",

        "CSS":
        "Practice Flexbox and Grid layouts",

        "JavaScript":
        "Build interactive websites",

        "React":
        "Create frontend React projects",

        "Node.js":
        "Build backend APIs",

        "Python":
        "Practice Python coding and projects",

        "Flask":
        "Build Python web applications",

        "SQL":
        "Practice database queries",

        "Git":
        "Learn version control using GitHub",

        "REST API":
        "Build API integration projects",


        # Cloud Engineer
        "AWS":
        "Deploy applications using AWS",

        "Azure":
        "Learn cloud infrastructure",

        "Linux":
        "Practice Linux commands",

        "Docker":
        "Build containerized applications",

        "Kubernetes":
        "Learn container orchestration",

        "Networking":
        "Study networking fundamentals",

        "Terraform":
        "Learn infrastructure automation",


        # Cyber Security Analyst
        "Wireshark":
        "Practice packet analysis",

        "Burp Suite":
        "Learn web application testing",

        "Nmap":
        "Practice network scanning",

        "Kali Linux":
        "Learn penetration testing tools",


        # Data Scientist
        "Machine Learning":
        "Build ML prediction projects",

        "Pandas":
        "Practice data cleaning and analysis",

        "NumPy":
        "Practice numerical computing",

        "TensorFlow":
        "Build Deep Learning models",

        "Statistics":
        "Study probability and statistics",


        # AI/ML Engineer
        "Deep Learning":
        "Build neural network projects",

        "PyTorch":
        "Practice AI model development",

        "NLP":
        "Work on text-processing projects",


        # UI/UX Designer
        "Figma":
        "Create UI designs",

        "Adobe XD":
        "Build design prototypes",

        "Wireframing":
        "Practice UI structure design",

        "Prototyping":
        "Build interactive designs",

        "User Research":
        "Learn user behavior analysis"
    }

    result = []

    for skill in missing_skills:

        if skill in suggestions:

            result.append(

                skill
                + " → " +
                suggestions[skill]

            )

        else:

            result.append(

                skill
                + " → Learn and practice this skill"

            )


    return result