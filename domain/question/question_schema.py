from datetime import datetime

from pydantic import BaseModel

__all__ = ["Question"]


class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime
