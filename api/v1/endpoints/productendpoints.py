from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse, Response


from database_engine.engine import get_db
from schemas.product_schema import Products, update_products
from helpers.oauth2 import get_current_user
from api.v1.controller import product_controller
from schemas.user_schema import UserBase
from helpers import response_parser, constants

router = APIRouter(prefix="/products")


@router.post("/")
def createProducts(
    request: Products,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user),
):
    try:
        return product_controller.create_products_controller(request, db, current_user)
    except Exception as e:
        if hasattr(e, "status_code"):
            raise e
        else:
            raise response_parser.generate_response(
                code=500, message=constants.BAD_REQUEST
            )


@router.get("/{id}")
def getProductByID(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user),
):
    try:
        return product_controller.get_products_by_id_controller(db, id, current_user)
    except Exception as e:
        if hasattr(e, "status_code"):
            raise e
        else:
            raise response_parser.generate_response(
                code=500, message=constants.BAD_REQUEST
            )


@router.get("/")
def get_all_products_endpoint(
    db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)
):
    try:
        return product_controller.get_all_products_controller(db=db)
    except Exception as e:
        if hasattr(e, "status_code"):
            raise e
        else:
            raise response_parser.generate_response(
                code=500, message=constants.BAD_REQUEST
            )


@router.put("/{id}")
def edit_Product(
    id: int,
    request: update_products,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user),
):
    try:
        return product_controller.edit_product_controller(id, db, current_user, request)
    except Exception as e:
        if hasattr(e, "status_code"):
            raise e
        else:
            raise response_parser.generate_response(
                code=500, message=constants.BAD_REQUEST
            )


@router.delete("/{id}")
def delete_product(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user),
):
    try:
        return product_controller.delete_product_controller(db, id, current_user)
    except Exception as e:
        if hasattr(e, "status_code"):
            raise e
        else:
            raise response_parser.generate_response(
                code=500, message=constants.BAD_REQUEST
            )
