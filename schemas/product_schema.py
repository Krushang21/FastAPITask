from typing import List, Optional
from pydantic import BaseModel
from marshmallow import fields, Schema, validate


# Products inside UserDisplay
class Products(BaseModel):
    title: str
    content: str

    class Config:
        from_attributes = True


class ProductsMarsh(Schema):
    title = fields.String(
        required=True,
        validate=validate.Regexp(
            r"^[a-zA-Z0-9\s\.,'!]{3,50}$",
            error="Product title should be between 3 to 50 characters",
        ),
    )
    content = fields.String(
        required=True,
        validate=validate.Regexp(r"^[a-zA-Z0-9\s\.,'!&$%#@*()-+=]{10,300}$"),
        error="Product Content should be minimum 10 and max 50 characters",
    )


class UpdateProductMarsh(Schema):
    title = fields.String(
        required=False,
        allow_none=True,
        validate=validate.Regexp(
            r"^[a-zA-Z0-9\s\.,'!]{3,50}$",
            error="Product title should be between 3 to 50 characters",
        ),
    )
    content = fields.String(
        required=False,
        allow_none=True,
        validate=validate.Regexp(r"^[a-zA-Z0-9\s\.,'!&$%#@*()-+=]{10,300}$"),
        error="Product Content should be minimum 10 and max 50 characters",
    )


class update_products(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None


class product_return(BaseModel):
    id: Optional[int]
    title: Optional[str]
    content: Optional[str]

    class Config:
        from_attributes = True


# class UserBase(BaseModel):
#     username: str
#     email: str
#     password: str
#     is_admin: bool = False


# class UpdateUserBase(BaseModel):
#     username: Optional[str] = None
#     email: Optional[str] = None
#     # password : Optional[str] = Nonse
