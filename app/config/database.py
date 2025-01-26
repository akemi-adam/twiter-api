from os import getenv

from sqlalchemy import create_engine, Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

Base = declarative_base()

engine: Engine = create_engine(getenv('DATABASE_URL'))
Base.metadata.create_all(engine)

def get_session() -> Session:
    return sessionmaker(bind=engine)()