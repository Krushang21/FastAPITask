from fastapi import Depends, status, HTTPException
import json
from fastapi.responses import JSONResponse
from sqlalchemy.orm.session import Session
from marshmallow import ValidationError

from database_engine.engine import get_db
from helpers.oauth2 import get_current_user
from helpers.password import Hash
from models import models
from helpers import response_parser, constants
from schemas.user_schema import (
    UserSchema,
    UserDisplay,
    UserBase,
    UpdateUserBase,
    ReadUserSchema,
    UserBaseMarsh,
    UpdateUserBaseMarsh,
)
from schemas import user_schema
from services.user_services import (
    create_user_service,
    read_all_users_service,
    get_user_by_id_service,
    get_user_by_username_service,
    update_user_service,
    delete_user_service,
    existing_user_check,
    get_user_by_username_service,
)


def create_user_controller(db: Session, request: UserBase, current_user):
    if current_user.is_admin:
        try:
            validated_data = UserBaseMarsh().load(dict(request))
            if not existing_user_check(db=db, request=request):
                hashed_password = Hash.bcrypt(request.password)
                new_user = models.User(
                    username=validated_data["username"],
                    email=validated_data["email"],
                    password=hashed_password,
                    is_admin=validated_data["is_admin"],
                )
                user = create_user_service(db, request, new_user)
                return response_parser.generate_response(
                    code=200,
                    message=constants.USER_CREATED_SUCCESS,
                )
            else:
                print("exist")
                raise response_parser.generate_response(
                    code=409, message=constants.USERNAME_CONFLICT
                )
        except ValidationError as e:
            raise response_parser.generate_response(
                code=422, message=constants.USER_VALIDATION_ERROR, data=e.messages
            )
        except Exception as err:
            raise err
    else:
        raise response_parser.generate_response(
            code=401, message=constants.ACCESS_DENIED
        )


def read_all_users_controller(
    db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)
):
    users = read_all_users_service(db, current_user)
    users_list = [vars(ReadUserSchema(**user.__dict__)) for user in users]
    if users_list:
        return response_parser.generate_response(code=200, data=users_list)
    else:
        return response_parser.generate_response(
            code=200, message=constants.USER_NOT_FOUND
        )


def get_user_by_id_controller(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user),
):
    if current_user.is_admin:
        user = get_user_by_id_service(id, db)
        if user:
            to_return = user_schema.UserDisplay(**user.__dict__).model_dump()
            return response_parser.generate_response(
                code=200, data=to_return, message=constants.USER_LIST
            )
        if not user:
            raise response_parser.generate_response(
                code=404, message=constants.USER_NOT_FOUND
            )
    else:
        raise response_parser.generate_response(
            code=401, message=constants.ACCESS_DENIED
        )


def get_user_by_username_controller(
    username: str,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user),
):
    if current_user.is_admin:
        user = get_user_by_username_service(db, username)
        if not user:
            raise response_parser.generate_response(
                code=404, message=constants.USER_NOT_FOUND
            )
        return response_parser.generate_response(code=200, data=user)
    else:
        raise response_parser.generate_response(
            code=401, message=constants.ACCESS_DENIED
        )


def update_user_controller(
    id: int,
    request: UpdateUserBase,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user),
):
    selected_user = get_user_by_id_service(id=id, db=db)
    if not current_user.is_admin:
        raise response_parser.generate_response(
            code=401, message=constants.ACCESS_DENIED
        )
    try:
        UpdateUserBaseMarsh().load(dict(request))
        if selected_user:
            if "username" in request.dict():
                new_username = request.dict()["username"]
                existing_user = get_user_by_username_service(
                    username=new_username, db=db
                )

                if existing_user and existing_user.id != id:
                    raise response_parser.generate_response(
                        code=409, message=constants.USERNAME_CONFLICT
                    )

                update_user_service(
                    id=id,
                    request=request,
                    db=db,
                    current_user=current_user,
                    selected_user=selected_user,
                )
                return response_parser.generate_response(
                    code=200, message=constants.USER_EDITED_SUCESS
                )
    except ValidationError as e:
        raise response_parser.generate_response(
            code=422,
            message=constants.USER_VALIDATION_ERROR,
        )
    else:
        raise response_parser.generate_response(
            code=404, message=constants.USER_NOT_FOUND
        )


def delete_user_controller(
    id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)
):
    if current_user.is_admin and current_user.id != id:
        selected_user = get_user_by_id_service(id=id, db=db)
        if selected_user:
            delete_user_service(selected_user=selected_user, db=db)
            return response_parser.generate_response(
                code=200, message=constants.USER_DELETED_SUCCESS
            )
        else:
            raise response_parser.generate_response(
                code=404, message=constants.USER_NOT_FOUND
            )
    elif current_user.is_admin and current_user.id == id:
        raise response_parser.generate_response(
            code=403, message=constants.USER_ACTION_FORBIDDEN
        )
    else:
        raise response_parser.generate_response(
            code=401, message=constants.ACCESS_DENIED
        )
