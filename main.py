from pydantic import BaseModel
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

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


class Item(BaseModel):
    name: str
    age: int | None = None


@app.get("/memo/{memo_id}")
async def showmethemoney(memo_id: int):
    return {"memo_id": memo_id}


@app.post("/memo")
async def operationcwal(item: Item):
    item.age += 10
    return item
