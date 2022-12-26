from fastapi import APIRouter, Query
from typing import Union, List
from Model import Item
from Enum import ModelName

router = APIRouter(prefix="/router", tags=["Router"])

# 路径操作是按顺序依次运行的。


# 声明一个可在 URL 中出现多次的查询参数 q，以一个 Python list 的形式接收到查询参数 q 的多个值。
# Query(default=[])
# Query(default=["foo", "bar"])
@router.get("/items/list")
async def items_list(q: Union[List[str], None] = Query(
    default=None,
    title="title",
    description="description",
    alias="q-q"
)):
    query_items = {"q": q}
    return query_items


@router.get("/items")
async def read_items(q: Union[str, None] = Query(default=None, min_length=1, max_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# 路径转换器。
@router.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


# 预设值: 指定路径参数的可用值。
@router.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.aaa:
        return {"model_name": model_name}

    if model_name.value == "bbb":
        return {"model_name": model_name}

    return {"model_name": model_name}


@router.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@router.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    # print(item.dict())    {'name': 'string', 'price': 0.0, 'is_offer': True}
    return {"item_name": item.name, "item_id": item_id}
