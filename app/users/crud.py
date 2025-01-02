from sqlalchemy.orm import Session
from app.users.models import User
from app.users.schemas import UserCreate
import bcrypt

def create_user(db: Session, user: UserCreate):
    hashed_password = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt())
    db_user = User(
        name=user.name,
        email=user.email,
        hashed_password=hashed_password.decode("utf-8")
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

