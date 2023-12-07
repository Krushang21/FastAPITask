# endpoints/authentication.py
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session

from database_engine.engine import get_db
from services.login_services import get_user
from helpers.password import Hash
from helpers import oauth2, response_parser, constants

router = APIRouter()


@router.post("/login")
def get_token(
    request: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
    # token: str = Depends(oauth2.oauth2_scheme),
):
    user = get_user(db, request.username)

    if not user:
        raise response_parser.generate_response(
            code=401, message=constants.INVALID_CREDENTIALS
        )

    if not Hash.verify(user.password, request.password):
        raise response_parser.generate_response(
            code=401, message=constants.INVALID_CREDENTIALS
        )

    if user.is_active == False:
        raise response_parser.generate_response(
            code=401, message=constants.ACCESS_DENIED
        )

    access_token = oauth2.create_access_token(data={"sub": str(user.id)})

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_type": user.is_admin,
    }
