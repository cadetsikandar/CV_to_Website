# app/users/dependencies.py
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.users.models import User

def get_current_user():
    # Dummy function for now, replace with your auth logic
    return User(id=1, email="test@example.com")
