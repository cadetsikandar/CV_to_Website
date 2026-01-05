# app/cvs/models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class CV(Base):
    __tablename__ = "cvs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    filename = Column(String, nullable=False)
    filepath = Column(String, nullable=False)
    website_url = Column(String, nullable=True)
    data_json = Column(String, nullable=True)        # flattened text for search/AI
    readable_text = Column(String, nullable=True)    # human-readable for preview

    owner = relationship("User", back_populates="cvs")
