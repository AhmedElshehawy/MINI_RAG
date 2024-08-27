import os
from fastapi import FastAPI, APIRouter


base_router = APIRouter(
    prefix='/api/v1', # all routes under this base router needs to be prefixed with this prefix 
    tags=['api_v1'] # add tags to these routers (useful in documentation)
)

@base_router.get("/")
async def welcome():
    app_name = os.getenv('APP_NAME')
    app_version = os.getenv('APP_VERSION')
    
    return {
        "app_name": app_name,
        "app_version": app_version
    }
