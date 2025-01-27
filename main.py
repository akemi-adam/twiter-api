from fastapi import FastAPI
from dotenv import load_dotenv

from app.config.database import Base, engine

load_dotenv()

Base.metadata.create_all(engine)

app = FastAPI()


@app.get("/")
async def root():
    return {}