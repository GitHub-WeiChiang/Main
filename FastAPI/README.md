FastAPI
=====
* ### uvicorn 是一個 ASGI 服务器。
* ### FastAPI 是直接从 Starlette 继承的类: Starlette is a lightweight ASGI framework / toolkit, which is ideal for building async web services in Python.
* ### Pydantic: Data validation and settings management using Python type annotations. Pydantic enforces type hints at runtime, and provides user-friendly errors when data is invalid.
* ### 在使用 Query 且需要声明一个值是必需的时，只需不声明默认参数或是使用省略号 Query(default=...) 声明必需参数。
* ### 官方表示，如果你很不爽 ...，也可以透過 Query(default=Required) 声明必需参数。
* ### Query 为查询参数校验，Path 为路径参数校验，Field 为 BaseModel 內的參數校验。
* ### 宣告函数時將带有「默认值」的参数放在没有「默认值」的参数之前，Python 将会报错，如果非得要當一個叛逆的孩子，可以传递 * 作为函数的第一个参数，使所有参数都应作为关键字参数 (键值对)，也被称为 kwargs 来调用。
* ### 可以使用 Body 指示 FastAPI 将所宣告參數作为请求体的另一个键进行处理。
* ### Body(embed=True) 可以使單一的 BaseModel 查询参数透過 request 傳遞至 FastAPI 時其 Json 具有鍵值。
* ### 从 typing 导入 List 可以声明具有子类型的列表。
* ### Python frozenset() 函数可以返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。
* ### 
<br />
