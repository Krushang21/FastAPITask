from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from marshmallow import ValidationError


from helpers import response_parser, constants
from schemas import product_schema
from services import product_services


def get_all_products_controller(db):
    products = product_services.get_all_products_service(db=db)
    products_list = [
        vars(product_schema.product_return(**product.__dict__)) for product in products
    ]
    if products_list:
        return response_parser.generate_response(
            code=200, data=products_list, message=constants.PRODUCT_CREATED_SUCCESS
        )
    else:
        return response_parser.generate_response(
            code=200, data=[], message=constants.PRODUCT_NOT_FOUND
        )


def create_products_controller(request, db, current_user):
    if current_user.is_admin:
        try:
            product_schema.ProductsMarsh().load(dict(request))
            product = product_services.create_products_service(
                request, db, current_user
            )
            if product:
                return response_parser.generate_response(
                    code=200, message=constants.PRODUCT_CREATED_SUCCESS
                )
            else:
                raise response_parser.generate_response(
                    coce=400, message=constants.BAD_REQUEST
                )
        except ValidationError as e:
            raise response_parser.generate_response(
                code=422, message=constants.PRODUCT_VALIDATION_ERROR
            )
    else:
        raise HTTPException(
            status.HTTP_403_FORBIDDEN,
            message=constants.ACCESS_DENIED,
        )


def get_products_by_id_controller(db: Session, id: int, current_user):
    if current_user.is_admin:
        product = product_services.get_products_by_id_service(db=db, id=id)
        if product:
            to_return = product_schema.product_return(**product.__dict__).model_dump()
            return response_parser.generate_response(
                code=200, data=to_return, message=constants.PRODUCTS_LIST
            )
        else:
            raise response_parser.generate_response(
                code=404, message=constants.PRODUCT_NOT_FOUND
            )
    else:
        raise response_parser.generate_response(
            code=403, message=constants.ACCESS_DENIED
        )


def edit_product_controller(db, id, current_user, request):
    if current_user.is_admin:
        try:
            product_schema.UpdateProductMarsh().load(dict(request))
            product = product_services.edit_product_service(db, id, request)
            if product:
                modified_fields = request.dict(exclude_unset=True)
                return response_parser.generate_response(
                    code=200,
                    message=constants.PRODUCT_EDITED_SUCCESS,
                )
            else:
                raise response_parser.generate_response(
                    code=404, message=constants.PRODUCT_NOT_FOUND
                )
        except ValidationError as e:
            raise response_parser.generate_response(
                code=422,
                message=constants.PRODUCT_VALIDATION_ERROR,
            )

    else:
        raise response_parser.generate_response(
            code=403, message=constants.ACCESS_DENIED
        )


def delete_product_controller(db, id, current_user):
    if current_user.is_admin:
        product = product_services.delete_product_service(db=db, id=id)
        if product:
            return response_parser.generate_response(
                code=200, message=constants.PRODUCT_DELETED_SUCCESS
            )
        raise response_parser.generate_response(
            code=404, message=constants.PRODUCT_NOT_FOUND
        )
    else:
        raise response_parser.generate_response(
            code=403, message=constants.ACCESS_DENIED
        )
