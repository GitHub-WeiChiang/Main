import uvicorn as uvicorn

from fastapi import FastAPI, Header, HTTPException, Depends
from Router import router
from starlette.responses import RedirectResponse


async def verify_token(x_token: str = Header()):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


# app = FastAPI(dependencies=[Depends(verify_token)])
app = FastAPI()


# 路径操作装饰器
@app.get("/", tags=["Main"])
async def root():
    return RedirectResponse("http://127.0.0.1:8000/docs#/")

app.include_router(router)


if __name__ == '__main__':
    uvicorn.run("Main:app", host="127.0.0.1", port=8000, reload=True)
