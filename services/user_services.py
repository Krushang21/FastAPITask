from fastapi import HTTPException, status, Depends
from fastapi.responses import JSONResponse
from helpers.password import Hash
from models.models import User
from database_engine.engine import get_db
from schemas.user_schema import UserBase
from sqlalchemy.orm.session import Session
from helpers import response_parser


def existing_user_check(db, request):
    try:
        # print("ExistService")
        existing_user = db.query(User).filter(User.username == request.username).first()
        return existing_user
    except Exception as e:
        raise response_parser.generate_response(code=400, message=constants.BAD_REQUEST)


def create_user_service(db, request, new_user):
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as e:
        raise response_parser.generate_response(code=400, message=constants.BAD_REQUEST)


def read_all_users_service(db, current_user):
    try:
        users = db.query(User).filter(User.is_active == True).all()
        return users
    except Exception as e:
        raise response_parser.generate_response(code=400, message=constants.BAD_REQUEST)


def get_user_by_id_service(db: Session, id: int):
    try:
        user = db.query(User).filter(User.id == id, User.is_active == 1).first()
        return user
    except Exception as e:
        raise response_parser.generate_response(code=400, message=constants.BAD_REQUEST)


def get_user_by_username_service(username: str, db: Session = Depends(get_db)):
    try:
        user = (
            db.query(User)
            .filter(User.username == username, User.is_active == True)
            .first()
        )
        return user
    except Exception as e:
        raise response_parser.generate_response(code=400, message=constants.BAD_REQUEST)


def update_user_service(id, request, db, current_user, selected_user):
    try:
        user = selected_user
        user_dict = request.dict(exclude_unset=True)
        for key, values in user_dict.items():
            if values is not None:
                setattr(user, key, values)
        db.commit()
        db.refresh(user)
        return user, None
    except Exception as e:
        raise response_parser.generate_response(code=400, message=constants.BAD_REQUEST)


def delete_user_service(db, selected_user):
    try:
        user = selected_user
        user.is_active = False
        db.commit()
        db.refresh(user)
        return user
    except Exception as e:
        raise response_parser.generate_response(code=400, message=constants.BAD_REQUEST)
