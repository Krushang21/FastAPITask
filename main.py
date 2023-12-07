from fastapi import FastAPI, APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from api.v1.endpoints import loginendpoint, userendpoints, productendpoints
from database_engine.engine import Base, engine

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)


@app.get("/")
def defaultpage():
    return JSONResponse(status_code=200, content="DefaultHomePage")


app.include_router(router=loginendpoint.router, tags=["Login"], prefix="/login")
app.include_router(router=userendpoints.router, tags=["Users"], prefix="/users")
app.include_router(router=productendpoints.router, tags=["Products"])

Base.metadata.create_all(bind=engine)
