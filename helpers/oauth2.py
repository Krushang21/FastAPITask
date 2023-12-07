from datetime import timedelta, datetime
from typing import Optional
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

from models.models import User
from jose import jwt, JWTError
from database_engine.engine import get_db
from services import user_services

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/login")


SECRET_KEY = "77407c7339a6c00544e51af1101c4abb4aea2a31157ca5f7dfd87da02a628107"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=1560)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate exception",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = int(payload.get("sub"))
        if user_id is None:
            raise credentials_exception
    except JWTError as e:
        raise credentials_exception
    user = user_services.get_user_by_id_service(db=db, id=user_id)

    if user is None:
        raise credentials_exception
    return user
