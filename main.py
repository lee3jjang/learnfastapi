from typing import Annotated
from pydantic import BaseModel
from fastapi import Depends, FastAPI
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from domain.answer import answer_router

from domain.question import question_router

app = FastAPI()


origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(question_router.router)
app.include_router(answer_router.router)


class Item(BaseModel):
    name: str
    age: int | None = None


def test_contextlib():
    print("Before try")
    x = {"name": "sangjin"}
    try:
        print("Before yield")
        yield x
        print("After yield")
    finally:
        print("Finally")


async def common_parameters(
    r: int = 30,
    q: str | None = None,
):
    return {"q": q, "r": r}


@app.get("/test/{test_id}")
async def showmethemoney(
    test_id: int,
    x: Session = Depends(test_contextlib),
    commons: Annotated[dict, Depends(common_parameters)] = dict,
):
    print(commons)
    print("showmethemoney")
    print(x, test_id)
    print("operationcwal")
    return {"test_id": test_id}


@app.post("/test")
async def operationcwal(item: Item):
    item.age += 10
    return item
