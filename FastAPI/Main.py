# ASGI 服务器
import uvicorn as uvicorn

from fastapi import FastAPI
from Router import router
from starlette.responses import RedirectResponse

app = FastAPI()


@app.get("/")
async def root():
    return RedirectResponse("http://127.0.0.1:8000/docs#/")

app.include_router(router)


if __name__ == '__main__':
    uvicorn.run("Main:app", host="127.0.0.1", port=8000, reload=True)
