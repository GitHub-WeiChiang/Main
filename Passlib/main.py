import jwt
import uvicorn

from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from passlib.context import CryptContext

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 25

fake_users_db = {
    "root": {
        "username": "root",
        "full_name": "root",
        "email": "root@gmail.com",
        "hashed_password": "$2b$12$pFjUldY11I0CS7WOgjraVOd7iCo8wbv.tUPCLZiXu5TGDoM9glYi2",
        "disabled": False,
    }
}


class Token(BaseModel):
    access_token: str
    token_type: str


class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


class UserInDB(User):
    hashed_password: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

app = FastAPI()


# 校验密码
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# # 密码哈希
# def get_password_hash(password):
#     # pwd_context.hash("root)
#     # $2b$12$pFjUldY11I0CS7WOgjraVOd7iCo8wbv.tUPCLZiXu5TGDoM9glYi2
#     return pwd_context.hash(password)


# 模拟从数据库读取用户信息
def get_user(db, username: str):
    user_dict = db.get(username, None)
    if user_dict:
        return UserInDB(**user_dict)


# 用户信息校验: username 和 password 分别校验
def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)

    if not user:
        return False

    if not verify_password(password, user.hashed_password):
        return False

    return user


# 生成 token，带有过期时间
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()

    # 有一个实效性，默认的时间 25 分钟
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    # 首先校验用户信息
    print(form_data.password)
    print(form_data.username)

    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # 生成并返回 token 信息
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        username: str = payload.get("sub")

        if username is None:
            raise credentials_exception
    except jwt.PyJWTError as ex:
        print(ex)
        raise credentials_exception

    user = get_user(fake_users_db, username=username)

    if user is None:
        raise credentials_exception

    return user


@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


if __name__ == '__main__':
    # print(pwd_context.hash("root"))
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
