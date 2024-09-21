import os
from typing import Dict
from fastapi import FastAPI, APIRouter, Depends
from helpers.config import get_settings, Settings


base_router = APIRouter(
    prefix='/api/v1', # all routes under this base router needs to be prefixed with this prefix 
    tags=['api_v1'] # add tags to these routers (useful in documentation)
)

@base_router.get("/")
async def welcome(app_settings: Settings = Depends(get_settings))-> Dict[str, str]: 
    app_name = app_settings.APP_NAME
    app_version = app_settings.APP_VERSION
    
    return {
        "app_name": app_name,
        "app_version": app_version
    }
