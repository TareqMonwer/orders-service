from sqlalchemy.orm import Session
from app.models.order import Order
from app.schemas.order import OrderCreate, OrderRead, OrderUpdate


def create_order(db: Session, order: OrderCreate) -> Order:
    """
    Create a new order in the database
    """
    db_order = Order(
        customer_id=order.customer_id,
        product_id=order.product_id,
        quantity=order.quantity,
        price=order.price,
        status=order.status or "pending"
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def get_order(db: Session, order_id: int) -> Order:
    """
    Get an order by ID
    """
    return db.query(Order).filter(Order.id == order_id).first()


def get_orders_by_user(db: Session, user_id: int) -> list[Order]:
    """
    Get all orders for a specific user (using customer_id as user identifier)
    """
    return db.query(Order).filter(Order.customer_id == user_id).all()


def update_order(db: Session, order_id: int, user_id: int, order_update: OrderUpdate) -> Order:
    """
    Update an order (only if it belongs to the user)
    """
    db_order = db.query(Order).filter(Order.id == order_id, Order.customer_id == user_id).first()
    if not db_order:
        return None
    
    # Update only provided fields
    update_data = order_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        if value is not None:
            setattr(db_order, field, value)
    
    db.commit()
    db.refresh(db_order)
    return db_order


def delete_order(db: Session, order_id: int, user_id: int) -> bool:
    """
    Delete an order (only if it belongs to the user)
    """
    db_order = db.query(Order).filter(Order.id == order_id, Order.customer_id == user_id).first()
    if not db_order:
        return False
    
    db.delete(db_order)
    db.commit()
    return True