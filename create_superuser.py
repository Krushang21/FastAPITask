from models.models import User
from database_engine.engine import get_db
from helpers.password import Hash
from sqlalchemy.orm import Session


def create_superuser(db: Session):
    superuser_data = {
        "username": "admin10",
        "email": "admin@crud.com",
        "is_admin": True,
        "password": "admin",
    }
    hashed_password = Hash.bcrypt(superuser_data["password"])
    superuser = User(
        username=superuser_data["username"],
        email=superuser_data["email"],
        is_admin=superuser_data["is_admin"],
        password=hashed_password,
    )
    db.add(superuser)
    db.commit()
    db.refresh(superuser)


db = next(get_db())
create_superuser(db)
