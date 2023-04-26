Passlib
=====
* ### 利用 PassLib 对入库的用户密码进行加密处理，推荐的加密算法是 Bcrypt。
    * ### passlib 是 Python 的密码散列库，提供超过 30 种密码散列算法的跨平台实现，以及作为管理现有密码哈希的框架。
    * ### bcrypt 模块是一个用于在 Python 中生成强哈希值的库。
    ```
    pip install passlib
    pip install bcrypt
    ```
* ### Demo (Postman)
    * ### Post - 127.0.0.1:8000/token
        * ### Body - form data
            * ### username - root
            * ### password - root
    * ### Get - 127.0.0.1:8000/users/me
        * ### Headers
            * ### Authorization - bearer "token value"
<br />
