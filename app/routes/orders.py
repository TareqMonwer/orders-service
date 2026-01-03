from app.schemas.order import OrderCreate, OrderRead, OrderPayload
from app.dependencies.auth import get_current_user
from fastapi import APIRouter, Depends
from pydantic import BaseModel


order_router = APIRouter(prefix="/orders", tags=["orders"])


@order_router.post("/", response_model=OrderRead)
def create_order(order: OrderPayload, current_user: dict = Depends(get_current_user)):
    """
    Create a new order with product_id=1, price=100, and user_id from authenticated token
    """
    user_id = current_user["user_id"]
    
    order = OrderCreate(
        customer_id=user_id,
        product_id=order.product_id,
        quantity=order.quantity,
        price=order.price
    )
    
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
