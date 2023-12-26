from datetime import datetime

from pydantic import BaseModel, field_validator

__all__ = [
    "AnswerCreate",
    "Answer",
]


class AnswerCreate(BaseModel):
    content: str

    @field_validator("content")
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("Empty value is not allowed")
        return v


class Answer(BaseModel):
    id: int
    content: str
    create_date: datetime
