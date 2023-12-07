from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from database_engine.engine import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), unique=True)
    email = Column(
        String(50),
    )
    password = Column(String(500))
    is_admin = Column(Boolean, default=False)
    items = relationship("Product", back_populates="user")
    is_active = Column(Boolean, default=True)


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    content = Column(String(50))
    created_by = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="items")
    is_active = Column(Boolean, default=True)
