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

    cleaned_text = clean_text(text)

    sections = detect_sections(cleaned_text)

    return cleaned_text, sections


def clean_text(text):

    text = text.lower()

    text = text.replace("•", " ")

    text = text.replace("-", " ")

    text = re.sub(r'\s+', ' ', text)

    return text


def detect_sections(text):

    sections = {

        "skills": "",
        "experience": "",
        "education": "",
        "projects": ""
    }

    lines = text.split(".")


    for line in lines:

        if "skill" in line:

            sections["skills"] += line

        elif "experience" in line:

            sections["experience"] += line

        elif "education" in line:

            sections["education"] += line

        elif "project" in line:

            sections["projects"] += line

    return sections