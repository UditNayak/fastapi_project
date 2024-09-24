from typing import List, Literal

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()


class FilterParams(BaseModel):
    model_config = {"extra": "forbid"}

    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: List[str] = []


@app.get("/items/")
async def read_items(
    limit: int = Query(100, gt=0, le=100),
    offset: int = Query(0, ge=0),
    order_by: Literal["created_at", "updated_at"] = Query("created_at"),
    tags: List[str] = Query(default_factory=list)
):
    filter_query = FilterParams(limit=limit, offset=offset, order_by=order_by, tags=tags)
    return filter_query
