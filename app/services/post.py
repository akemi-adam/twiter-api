from fastapi import Depends

from sqlalchemy.orm import Session

from app.config.database import get_session


class PostService:
    def __init__(self, session: Session):
        self.session = session

        
        
def get_post_service(session: Session = Depends(get_session)):
    return PostService(session=session)