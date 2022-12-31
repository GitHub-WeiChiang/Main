from fastapi import APIRouter, Query, Body, Cookie, Form, HTTPException, Depends, Header
from typing import Union, List
from Model import Item, Item2, User, UserIn, UserOut
from Enum import ModelName
from fastapi.encoders import jsonable_encoder

router = APIRouter(prefix="/router", tags=["Router"])

# 路径操作是按顺序依次运行的。


async def verify_token(x_token: str = Header()):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


@router.get("/item15/", dependencies=[Depends(verify_token)])
async def item15():
    return [{"item": "Foo"}, {"item": "Bar"}]


@router.get("/item14/")
async def item14(x_token: Union[List[str], None] = Header(default=None)):
    return {"X-Token values": x_token}


# 依赖项
async def common_parameters(q: Union[str, None] = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


class CommonQueryParams:
    def __init__(self, q: Union[str, None] = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@router.get("/item13/")
async def item13(commons: CommonQueryParams = Depends()):
    resp: dict = {
        1: id(commons),
        2: id(Depends(CommonQueryParams))
    }
    return resp


@router.get("/item12/")
async def item12(commons: CommonQueryParams = Depends(CommonQueryParams)):
    return id(commons)


@router.get("/item11/")
async def item11(commons: dict = Depends(common_parameters)):
    return id(commons)


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@router.patch("/item10/{item_id}", response_model=Item2)
async def update_item(item_id: str, item: Item2):
    # # 更新數據中不包含的鍵值對會保留原有已經存在的值。
    # stored_item_data = items[item_id]
    # stored_item_model = Item2(**stored_item_data)
    # update_data = item.dict(exclude_unset=True)
    # updated_item = stored_item_model.copy(update=update_data)
    # items[item_id] = jsonable_encoder(updated_item)
    # return updated_item

    # 更新數據中不包含的鍵值對會強制被還原成預設值 (若有設定預設值)。
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded


@router.get("/item9", deprecated=True)
async def item9(item_id: str):
    raise HTTPException(status_code=404, detail="Item not found")


@router.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}


@router.post("/user/", response_model=UserOut, status_code=200)
async def create_user(user: UserIn):
    return user


@router.get("/item8")
async def item8(ads_id: Union[str, None] = Cookie(default=None)):
    return {"ads_id": ads_id}


# 声明一个可在 URL 中出现多次的查询参数 q，以一个 Python list 的形式接收到查询参数 q 的多个值。
# Query(default=[])
# Query(default=["foo", "bar"])
@router.get("/item7/list")
async def item7(q: Union[List[str], None] = Query(
    default=None,
    title="title",
    description="description",
    alias="q-q"
)):
    query_items = {"q": q}
    return query_items


@router.get("/item6")
async def item6(q: Union[str, None] = Query(default=None, min_length=1, max_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# 路径转换器。
@router.get("/item5/{file_path:path}")
async def item5(file_path: str):
    return {"file_path": file_path}


# 预设值: 指定路径参数的可用值。
@router.get("/item4/{model_name}")
async def item4(model_name: ModelName):
    if model_name is ModelName.aaa:
        return {"model_name": model_name}

    if model_name.value == "bbb":
        return {"model_name": model_name}

    return {"model_name": model_name}


@router.get("/item3/{item_id}")
async def item3(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@router.put("/item2")
async def item2(item: Item = Body(embed=True)):
    # print(item.dict())    {'name': 'string', 'price': 0.0, 'is_offer': True}
    return {"item_name": item.name}


@router.put("/item1/{item_id}")
async def item1(item_id: int, item: Item, user: User, importance: int = Body()):
    # print(item.dict())    {'name': 'string', 'price': 0.0, 'is_offer': True}
    return {"item_name": item.name, "item_id": item_id}
