from fastapi import Depends, HTTPException

from sqlalchemy.orm import Session

from app.models.post import Post
from app.config.database import get_session


class PostService:
    def __init__(self, session: Session):
        self.session = session
    
    def create(self, post_create):
        with self.session:
            post = Post(**post_create.model_dump())
            self.session.add(post)
            self.session.commit()
            self.session.refresh(post)
        return post
    
    def get_all(self):
        with self.session:
            posts = self.session.query(Post).all()
        return posts
    
    def get(self, id: int):
        with self.session:
            post = self.session.query(Post).get(id)
        return post
    
    def update(self):
        pass
    
    def delete(self, id: int) -> None:
        post = self.get(id)
        if post == None:
            raise HTTPException(status_code=404, detail="Post not found")
        self.session.delete(post)
        self.session.commit()
        
        
def get_post_service(session: Session = Depends(get_session)):
    return PostService(session=session)