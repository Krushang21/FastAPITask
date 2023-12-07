# services.py
from sqlalchemy.orm.session import Session
from models import models
from helpers.password import Hash


def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()
