# app/cvs/crud.py
from sqlalchemy.orm import Session
from app.cvs.models import CV
import pdfplumber
from docx import Document

def parse_cv(file_path: str) -> str:
    if file_path.endswith(".pdf"):
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return text
    elif file_path.endswith(".docx"):
        doc = Document(file_path)
        return "\n".join([p.text for p in doc.paragraphs])
    else:
        return ""



def create_cv(db: Session, user_id: int, filename: str, filepath: str, data_json: str, readable_text: str):
    cv_record = CV(
        user_id=user_id,
        filename=filename,
        filepath=filepath,
        data_json=data_json,
        readable_text=readable_text
    )
    db.add(cv_record)
    db.commit()
    db.refresh(cv_record)
    return cv_record


# def create_cv(db, user_id, filename, filepath, data_json):
#     cv = CV(
#         user_id=user_id,
#         filename=filename,
#         filepath=filepath,
#         data_json=data_json
#     )
#     db.add(cv)
#     db.commit()
#     db.refresh(cv)
#     return cv
