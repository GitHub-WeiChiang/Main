# 标准的 Python 类型声明请求体
from pydantic import BaseModel
# 联合类型
from typing import Union


class Item(BaseModel):
    name: str
    price: float
    # Union[X, Y] 等价于 X | Y ，意味着满足 X 或 Y 之一。
    is_offer: Union[bool, None] = None
