import uvicorn as uvicorn

from fastapi import FastAPI
from starlette.responses import RedirectResponse


app = FastAPI()


@app.get("/", tags=["Main"])
async def root():
    return RedirectResponse("http://127.0.0.1:8000/docs#/")


if __name__ == '__main__':
    uvicorn.run("Main:app", host="127.0.0.1", port=8000, reload=True)
