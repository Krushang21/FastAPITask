from fastapi import FastAPI
from models.models import Product
from schemas.product_schema import Products
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from helpers import response_parser, constants


def create_products_service(request, db, current_user):
    newProducts = Product(
        title=request.title, content=request.content, created_by=current_user.id
    )
    try:
        db.add(newProducts)
        db.commit()
        db.refresh(newProducts)
        return newProducts
    except Exception as e:
        raise response_parser.generate_response(code=400, message=constants.BAD_REQUEST)


def get_products_by_id_service(id: int, db: Session):
    try:
        product = (
            db.query(Product)
            .filter(Product.id == id, Product.is_active == True)
            .first()
        )
        return product
    except Exception as e:
        raise response_parser.generate_response(code=400, message=constants.BAD_REQUEST)


def edit_product_service(id, db, request):
    try:
        product = (
            db.query(Product)
            .filter(Product.id == id, Product.is_active == True)
            .first()
        )
        if product:
            product_dict = request.dict(exclude_unset=True)
            for field, value in product_dict.items():
                if value is not None:
                    setattr(product, field, value)
            db.commit()
            db.refresh(product)
            return product
        else:
            return None
        return product
    except Exception as e:
        raise response_parser.generate_response(code=400, message=constants.BAD_REQUEST)


def delete_product_service(id, db):
    try:
        product = (
            db.query(Product)
            .filter(Product.id == id, Product.is_active == True)
            .first()
        )
        if product:
            product.is_active = False
            db.commit()
            return product
    except Exception as e:
        raise response_parser.generate_response(code=400, message=constants.BAD_REQUEST)


def get_all_products_service(db):
    try:
        products = db.query(Product).filter(Product.is_active == True).all()
        return products
    except Exception as e:
        raise response_parser.generate_response(code=400, message=constants.BAD_REQUEST)
