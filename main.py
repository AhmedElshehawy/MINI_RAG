from fastapi import FastAPI
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
from routes import base


app = FastAPI()
app.include_router(base.base_router)
