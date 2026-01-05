from sqlalchemy.orm import Session
from app.users.models import User
from app.core.security import hash_password

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, email: str, password: str):
    db_user = User(email=email, password_hash=hash_password(password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
