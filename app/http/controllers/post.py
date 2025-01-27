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


@router.get("/")
async def get_all(postService: PostService = PostDep) -> List[PostOut]:
    return [PostOut(**post.__dict__) for post in postService.get_all()]


@router.get("/{id}")
async def get(id: int, postService: PostService = PostDep) -> PostOut:
    post = postService.get(id)
    return PostOut(**post.__dict__)

@router.delete("/{id}")
async def delete(id: int, postService: PostService = PostDep) -> dict:
    postService.delete(id)
    return {"message": f"Post with id {id} was deleted successfully"}