from app.schemas.order import OrderCreate
from fastapi import APIRouter
from pydantic import BaseModel


order_router = APIRouter(prefix="/orders", tags=["orders"])


@order_router.post("/", response_model=OrderCreate)
def create_order(order: OrderCreate):
    return order


@order_router.get("/", response_model=list[OrderCreate])
def get_orders():
    return []


@order_router.get("/{order_id}", response_model=OrderCreate)
def get_order(order_id: int):
    return OrderCreate(id=order_id)


@order_router.put("/{order_id}", response_model=OrderCreate)
def update_order(order_id: int, order: OrderCreate):
    return order


@order_router.delete("/{order_id}")
def delete_order(order_id: int):
    return {"order_id": order_id}
