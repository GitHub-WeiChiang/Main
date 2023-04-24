import uvicorn as uvicorn

from Security import create_access_token
from Security import check_jwt_token
from pydantic import BaseModel
from fastapi import FastAPI, Depends
from starlette.responses import RedirectResponse
from typing import Any, Union

app = FastAPI()


class UserInfo(BaseModel):
    username: str
    password: str


@app.post("/login/access-token", summary="用户登录认证")
async def login_access_token(user_info: UserInfo):
    # 登入流程...

    # 登录 token 只存放了 username
    return {
        "token": create_access_token(user_info.username),
    }


@app.get("/user/info", summary="获取用户信息")
async def get_user_info(token_data: Union[str, Any] = Depends(check_jwt_token)):
    print(token_data)

    # 这个状态能响应说明 token 验证通过
    return {
        "info": token_data
    }


# 路径操作装饰器
@app.get("/", tags=["Main"])
async def root():
    return RedirectResponse("http://127.0.0.1:8000/docs#/")

if __name__ == '__main__':
    uvicorn.run("Main:app", host="127.0.0.1", port=8000, reload=True)
