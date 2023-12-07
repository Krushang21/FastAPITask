from typing import List, Optional
from pydantic import BaseModel
from marshmallow import fields, validate, Schema

from schemas.product_schema import Products


class UserBase(BaseModel):
    username: str
    email: str
    password: str
    is_admin: bool = False


class UserBaseMarsh(Schema):
    username = fields.Str(
        required=True,
        # validate=[
        #     validate.Regexp(
        #         r"^[a-zA-Z0-9_-]$",
        #         error="Username must be 3-20 characters long and can only contain letters, numbers, underscores, and hyphens.",
        #     ),
        # ],
    )
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    is_admin = fields.Bool(required=True)


class UserDisplay(BaseModel):
    id: int
    username: str
    email: str
    is_admin: bool

    class Config:
        from_attributes = True


class UserSchema(BaseModel):
    username: str
    email: str

    class Config:
        from_attributes = True


class UpdateUserBase(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None

    class Config:
        from_attributes = True


class UpdateUserBaseMarsh(Schema):
    username = fields.String(
        required=False,
        allow_none=True,
        validate=validate.Regexp(
            r"^[a-zA-Z0-9_-]{3,20}$",
            error="Username must be 3-20 characters long and can only contain letters, numbers, underscores, and hyphens.",
        ),
    )
    email = fields.Email(required=False, allow_none=True)


class ReadUserSchema(BaseModel):
    id: int
    username: Optional[str] = None
    email: Optional[str] = None
