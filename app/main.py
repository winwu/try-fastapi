from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    # http://127.0.0.1:8000/
    return {"Hello": "World"}

@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str, None] = None):
    # http://127.0.0.1:8000/items/1?q=sdsf
    return {"item_id": item_id, "q": q}