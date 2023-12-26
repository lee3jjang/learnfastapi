from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def hello():
    return {"mesasge": "안녕하세요 파이보"}


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
