from sqlalchemy.orm import Session
from app.models.order import Order
from app.schemas.order import OrderCreate, OrderRead


def create_order(db: Session, order: OrderCreate) -> Order:
    """
    Create a new order in the database
    """
    db_order = Order(
        customer_id=order.customer_id,
        product_id=order.product_id,
        quantity=order.quantity,
        price=order.price
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
    Get all orders for a specific user
    """
    return db.query(Order).filter(Order.user_id == user_id).all()


def get_all_orders(db: Session) -> list[Order]:
    """
    Get all orders
    """
    return db.query(Order).all()