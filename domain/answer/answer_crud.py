from datetime import datetime

from sqlalchemy.orm import Session

from domain.answer.answer_schema import AnswerCreate
from models import Question, Answer


__all__ = ["create_answer"]


def create_answer(
    db: Session,
    question: Question,
    answer_create: AnswerCreate,
):
    answer = Answer(
        question=question,
        content=answer_create.content,
        create_date=datetime.now(),
    )
    db.add(answer)
    db.commit()
