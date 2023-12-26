from datetime import datetime

from pydantic import BaseModel, validator

from domain.answer.answer_schema import Answer

__all__ = ["Question"]


class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime
    answers: list[Answer] = []


class QuestionCreate(BaseModel):
    subject: str
    content: str

    @validator("subject", "content")
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("Empty value is not allowed")
        return v


class QuestionList(BaseModel):
    total: int = 0
    question_list: list[Question] = list
