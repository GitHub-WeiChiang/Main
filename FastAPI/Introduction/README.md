Introduction
=====
* ### uvicorn 是一個 ASGI 服务器。
* ### FastAPI 是直接从 Starlette 继承的类
    * ### Starlette is a lightweight ASGI framework / toolkit, which is ideal for building async web services in Python.
* ### Pydantic
    * ### Data validation and settings management using Python type annotations.
    * ### Pydantic enforces type hints at runtime, and provides user-friendly errors when data is invalid.
* ### 在使用 Query 且需要声明一个值是必需的时，只需不声明默认参数或是使用省略号 Query(default=...) 声明必需参数。
* ### 官方表示，如果你很不爽 ...，也可以透過 Query(default=Required) 声明必需参数。
* ### Query 为查询参数校验，Path 为路径参数校验，Field 为 BaseModel 內的參數校验。
* ### 宣告函数時將带有「默认值」的参数放在没有「默认值」的参数之前，Python 将会报错，如果非得要當一個叛逆的孩子，可以传递 * 作为函数的第一个参数，使所有参数都应作为关键字参数 (键值对)，也被称为 kwargs 来调用。
* ### 可以使用 Body 指示 FastAPI 将所宣告參數作为请求体的另一个键进行处理。
* ### Body(embed=True) 可以使單一的 BaseModel 查询参数透過 request 傳遞至 FastAPI 時其 Json 具有鍵值。
* ### 从 typing 导入 List 可以声明具有子类型的列表。
* ### Python frozenset() 函数可以返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。
* ### 可以在任意的路径操作中使用 response_model 参数来声明用于响应的模型。
* ### 可以使用 response_model_exclude_unset 参数忽略無实际值時的默認值。
* ### 使用路径操作装饰器的 response_model_include 和 response_model_exclude 参数，接收一个由属性名称 str 组成的 set 来包含或者排除这些属性。
* ### 可以在以下任意的路径操作中使用 status_code 参数来声明用于响应的 HTTP 状态码。
* ### 可以使用来自 fastapi.status 的 HTTP 响应状态码便捷变量。
* ### 使用 UploadFile 定义客户端的上传文件。
* ### 向客户端返回 HTTP 错误响应，可以使用 HTTPException，另因其是 Python 异常，所以不能 return，只能 raise。
* ### 可以使用 from starlette import status 导入状态码，用于定义路径操作响应的 HTTP 状态码，参数应直接传递给路径操作装饰器。
* ### tags 参数是由 str 组成的 list (一般只有一个 str)，用于为路径操作添加标签。
* ### response_description 参数用于定义响应的描述说明。
* ### jsonable_encoder 可以將數據類型 (如: Pydantic 模型) 轉換爲與 JSON 兼容的類型 (如: 字典、列表)。
* ### 使用 Pydantic 的 exclude_unset 参数更新部分数据，可以在 Pydantic 模型的 .dict() 中使用 exclude_unset 参数，生成的 dict 只包含创建 item 模型时显式设置的数据，而不包括默认值。
* ### 依赖注入常用于以下场景
    * ### 共享业务逻辑（复用相同的代码逻辑）
    * ### 共享数据库连接
    * ### 实现安全、验证、角色权限
* ### 當 Depends 依賴注入中是放入類別 (class) 且透過參數注入所需方法，其會以 Singleton 方式生成該注入類別實例。
* ### 依賴注入 (Dependency Injection)
    * ### 是一種軟體設計模式，也是實現控制反轉的其中一種技術，這種模式能讓一個物件接收它所依賴的其他物件。「依賴」是指接收方所需的物件，「注入」是指將「依賴」傳遞給接收方的過程。在「注入」之後，接收方才會呼叫該「依賴」。此模式確保了任何想要使用給定服務的物件不需要知道如何建立這些服務。
    * ### IoC (Inversion of Control，控制反轉): 減低電腦代碼之間的耦合度，將依賴的控制從內部轉至外部，最常見的方式叫做依賴注入 (Dependency Injection，簡稱 DI)。
    * ### DI (Dependency Injection，依賴注入): 將一個程式的相依關係改由呼叫它的外部程式來決定的方法。
    * ### 優點: 低耦合高內聚、更清晰的意圖、降低邏輯變更造成改動程式碼的幅度、關注點分離提高可測試性。
    * ### 缺點: 系統架構的複雜度增加。
* ### 使用 OAuth2PasswordBearer 类實現 OAuth2 的 Password 流以及 Bearer 令牌 (Token)。
* ### 透過 passlib 實作密码哈希和身份校验的功能。
* ### 透過 SQLAlchemy 實現數據庫操作。
* ### 文件结构示例
    * ### app
        * ### __init__.py
        * ### main.py
        * ### dependencies.py
        * ### routers
            * ### __init__.py
            * ### ...
        * ### internal
            * ### __init__.py
            * ### ...
* ### FastAPI 默认使用 JSONResponse 返回一个响应 (默认会使用 jsonable_encoder 将这些类型的返回值转换成 JSON 格式)。
* ### 以在路径函数中定义一个类型为 Response 的参数，这样你就可以在这个临时响应对象中设置 cookie 了 (还可以在直接响应 Response 时直接创建 cookies)。
```
@app.post("/")
def create_cookie(response: Response):
    response.set_cookie(key="", value="")
    
@app.post("/")
def create_cookie():
    response = JSONResponse(content=content)
    response.set_cookie(key="", value=")
    return response
```
* ### 自定义响应
    * ### PlainTextResponse: 接受文本或字节并返回纯文本响应。
    * ### JSONResponse: 接受数据并返回一个 application / json 编码的响应。
    * ### RedirectResponse: 返回 HTTP 重定向。默认情况下使用 307 状态代码 (临时重定向)。
    * ### StreamingResponse: 类似文件的对象 (例如，由 open() 返回的对象)，则可以在 StreamingResponse 中将其返回。包括许多与云存储，视频处理等交互的库。
    * ### FileResponse: 异步传输文件作为响应。
* ### 启用 HTTPS
    * ### 一般要用到: xxx.top.key (私钥文件) 和 xxx.yyy_bundle.crt (证书文件) 这两个文件，
    * ### 使用 ssl_keyfile 参数和 ssl_certfile 分别指定私钥和证书。
    ```
    uvicorn.run(
        app="project:app",
        host=host,
        port=port,
        reload=True,
        ssl_keyfile="./ssl/xxx.top.key",
        ssl_certfile="./ssl/xxx.top_bundle.crt"
    )
    ```
<br />

Reference
=====
* ### [FastAPI](https://fastapi.tiangolo.com/)
<br />
