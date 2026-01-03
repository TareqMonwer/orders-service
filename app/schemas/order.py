from pydantic import BaseModel, EmailStr
from typing import Optional


class OrderBase(BaseModel):
    customer_id: int
    product_id: int
    quantity: int
    price: float

class OrderCreate(OrderBase):
    pass
