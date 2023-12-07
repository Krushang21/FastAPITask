from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from database_engine.engine import get_db
from schemas.user_schema import UpdateUserBase, UserDisplay, UserBase
from helpers.oauth2 import get_current_user
from api.v1.controller import usercontroller
from helpers import response_parser, constants

router = APIRouter()


@router.post("/", response_model=UserBase)
def create_user_endpoint(
    request: UserBase,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user),
):
    try:
        return usercontroller.create_user_controller(db, request, current_user)
    except Exception as e:
        if hasattr(e, "status_code"):
            raise e
        else:
            raise response_parser.generate_response(
                code=500, message=constants.BAD_REQUEST
            )


@router.get("/", response_model=List[UserDisplay])
def readAllUsers_endpoint(
    db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)
):
    try:
        users = usercontroller.read_all_users_controller(db, current_user)
        return users
    except Exception as e:
        if hasattr(e, "status_code"):
            raise e
        else:
            raise response_parser.generate_response(
                code=500, message=constants.BAD_REQUEST
            )


@router.get("/{id}")
def readUserById_endpoint(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user),
):
    try:
        return usercontroller.get_user_by_id_controller(db, id, current_user)
    except Exception as e:
        if hasattr(e, "status_code"):
            raise e
        else:
            raise response_parser.generate_response(
                code=500, message=constants.BAD_REQUEST
            )


def readUserByUsername_endpoint(
    username: str,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user),
):
    try:
        return usercontroller.get_user_by_username_controller(
            db, username, current_user
        )
    except Exception as e:
        if hasattr(e, "status_code"):
            raise e
        else:
            raise response_parser.generate_response(
                code=500, message=constants.BAD_REQUEST
            )


@router.put("/{id}")
def updateUser_endpoint(
    id: int,
    request: UpdateUserBase,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user),
):
    try:
        return usercontroller.update_user_controller(
            db=db, id=id, request=request, current_user=current_user
        )
    except Exception as e:
        raise e
    else:
        if hasattr(e, "status_code"):
            raise response_parser.generate_response(
                code=500, message=constants.BAD_REQUEST
            )


@router.delete("/{id}")
def deleteUser_endpoint(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user),
):
    try:
        return usercontroller.delete_user_controller(
            db=db, id=id, current_user=current_user
        )
    except Exception as e:
        if hasattr(e, "status_code"):
            raise e
        else:
            raise response_parser.generate_response(
                code=500, message=constants.BAD_REQUEST
            )
