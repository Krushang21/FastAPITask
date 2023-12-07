from fastapi import APIRouter

from endpoints import userendpoints, loginendpoint, productendpoints

router = APIRouter()
router.include_router(router=loginendpoint.router, tags=["Login"], prefix="/login")
router.include_router(router=userendpoints.router, tags=["Users"])
app.include_router(
    router=productendpoints.router,
)
