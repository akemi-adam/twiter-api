from fastapi import Depends

from app.config.database import get_session

Session = Depends(get_session)