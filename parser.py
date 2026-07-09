from PyPDF2 import PdfReader
from docx import Document
import re


def extract_text(filepath):

    text = ""

    if filepath.endswith(".pdf"):

        reader = PdfReader(filepath)

        for page in reader.pages:

            extracted = page.extract_text()

            if extracted:

                text += extracted + "\n"

    elif filepath.endswith(".docx"):

        doc = Document(filepath)

        for paragraph in doc.paragraphs:

            text += paragraph.text + "\n"

    sections = detect_sections(text)

    cleaned_text = clean_text(text)

    return cleaned_text, sections


def clean_text(text):

    text = text.lower()

    text = text.replace("•", " ")

    text = text.replace("-", " ")

    text = re.sub(r"\s+", " ", text)

    return text


def detect_sections(text):

    sections = {

        "summary": "",
        "skills": "",
        "experience": "",
        "education": "",
        "projects": "",
        "certifications": "",
        "achievements": ""

    }

    current_section = None

    lines = text.splitlines()

    for line in lines:

        stripped = line.strip()

        if stripped == "":

            continue

        lower = stripped.lower()

        # ---------- SUMMARY ----------

        if lower in [

            "professional summary",
            "summary",
            "career objective",
            "objective",
            "profile",
            "about me"

        ]:

            current_section = "summary"

            continue

        # ---------- SKILLS ----------

        elif lower in [

            "skills",
            "technical skills",
            "key skills"

        ]:

            current_section = "skills"

            continue

        # ---------- EXPERIENCE ----------

        elif lower in [

            "experience",
            "work experience",
            "professional experience",
            "employment"

        ]:

            current_section = "experience"

            continue

        # ---------- EDUCATION ----------

        elif lower in [

            "education",
            "academic qualification",
            "qualification"

        ]:

            current_section = "education"

            continue

        # ---------- PROJECTS ----------

        elif lower in [

            "projects",
            "academic projects",
            "personal projects"

        ]:

            current_section = "projects"

            continue

        # ---------- CERTIFICATIONS ----------

        elif lower in [

            "certifications",
            "certificates",
            "licenses"

        ]:

            current_section = "certifications"

            continue

        # ---------- ACHIEVEMENTS ----------

        elif lower in [

            "achievements",
            "awards",
            "honors"

        ]:

            current_section = "achievements"

            continue

        if current_section:

            sections[current_section] += stripped + "\n"

    return sections