from app.config.database import Base

from sqlalchemy import Column, String, Text, Integer


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(Text)
    