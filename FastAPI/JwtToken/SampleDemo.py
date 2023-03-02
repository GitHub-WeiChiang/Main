from datetime import datetime, timedelta
from jose import jwt
from jose.exceptions import ExpiredSignatureError, JWTError

# 加密密钥
SECRET_KEY = "albert0425369@gmail.com"

# 设置过期时间
expire = datetime.utcnow() + timedelta(minutes=5)

# data
to_encode = {"exp": expire, "sub": "sub", "uid": "uid"}

# 生成token
encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")

if __name__ == '__main__':
    print(encoded_jwt)

    # -----

    payload = jwt.decode(
        encoded_jwt,
        "albert0425369@gmail.com",
        algorithms="HS256"
    )
    print(payload)

    # -----

    import time
    time.sleep(10)

    try:
        payload = jwt.decode(
            encoded_jwt,
            SECRET_KEY,
            algorithms="HS256"
        )
        print(payload)
    except ExpiredSignatureError as e:
        print("token 过期")
    except JWTError as e:
        print("token 验证失败")
