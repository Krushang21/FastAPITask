# engine.py

from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from helpers import get_env_vars

get_var = get_env_vars.get_settings()

db_string = f"mysql+pymysql://{get_var.mysql_user}:{get_var.mysql_pass}@{get_var.mysql_host}:{get_var.mysql_port}/{get_var.mysql_db}"


# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/crud"
engine = create_engine(db_string)
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
