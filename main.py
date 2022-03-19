from typing import Optional
import text2emotion as te
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/text/{text}")
def read_item(text: Optional[str]):
    result = te.get_emotion(text);
    return result;
