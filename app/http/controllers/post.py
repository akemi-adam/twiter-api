from fastapi import APIRouter, Depends

from typing import List

from app.http.requests.post import PostCreate, PostOut
from app.services.post import PostService, get_post_service


router = APIRouter(prefix="/posts")
PostDep = Depends(get_post_service)


@router.post("/")
async def create(request: PostCreate, postService: PostService = PostDep) -> PostOut:
    post = postService.create(request)
    return PostOut(**post.__dict__)


