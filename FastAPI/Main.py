# ASGI 服务器
import uvicorn as uvicorn

from fastapi import FastAPI
from Router import router
from starlette.responses import RedirectResponse

# FastAPI 是直接从 Starlette 继承的类
# Starlette is a lightweight ASGI framework / toolkit, which is ideal for building async web services in Python.
app = FastAPI()


# 路径操作装饰器
@app.get("/")
async def root():
    return RedirectResponse("http://127.0.0.1:8000/docs#/")

app.include_router(router)


if __name__ == '__main__':
    uvicorn.run("Main:app", host="127.0.0.1", port=8000, reload=True)
