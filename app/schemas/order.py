from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class OrderBase(BaseModel):
    product_id: int
    quantity: int
    price: float


class OrderPayload(OrderBase):
    status: Optional[str] = "pending"  # pending, processing, completed, cancelled


class OrderCreate(OrderBase):
    customer_id: int
    status: Optional[str] = "pending"


class OrderUpdate(BaseModel):
    product_id: Optional[int] = None
    quantity: Optional[int] = None
    price: Optional[float] = None
    status: Optional[str] = None  # pending, processing, completed, cancelled


class OrderRead(OrderBase):
    id: int
    customer_id: int
    status: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
