from typing import Union

import uvicorn as uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse

app = FastAPI()


@app.get("/")
async def root():
    return RedirectResponse("http://127.0.0.1:8000/docs#/")


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
