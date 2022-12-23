from fastapi import APIRouter
from typing import Union
from Model import Item

router = APIRouter(prefix="/router", tags=["Router"])


@router.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@router.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
