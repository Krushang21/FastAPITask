import logging
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import status, HTTPException

from schemas import api_response

logger = logging.getLogger(__name__)


def generate_response(
    code=status.HTTP_200_OK,
    message=None,
    data=[],
    headers={},
    success=True,
    media_type="application/json",
):
    try:
        if code not in [200, 201, 202, 204]:
            return HTTPException(
                status_code=code,
                detail=jsonable_encoder(
                    api_response.ApiResponse(
                        status_code=code,
                        message=str(message),
                        data=data,
                        success=success,
                    ).__dict__
                ),
            )
        else:
            return JSONResponse(
                status_code=code,
                media_type=media_type,
                headers=headers,
                content=jsonable_encoder(
                    api_response.ApiResponse(
                        status_code=code, message=message, data=data, success=success
                    ).__dict__
                ),
            )
    except Exception as err:
        logger.error("Error occurred in generate_response: %s", err, exc_info=True)
