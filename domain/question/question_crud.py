from sqlalchemy.orm import Session

from models import Question


__all__ = ["get_question_list"]


def get_question_list(db: Session):
    question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    return question_list
