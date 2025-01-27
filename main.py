from fastapi import FastAPI
from dotenv import load_dotenv

from app.http.controllers import post_router
from app.config.database import Base, engine

load_dotenv()

Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(prefix='/api/v1', router=post_router)