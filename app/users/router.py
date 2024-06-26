from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache

from app.auth.dependencies import get_current_user
from app.users.models import User
from app.users.schemas import SUserGet

router = APIRouter(tags=["Users"], prefix="/user")


@router.get("/me", response_model=SUserGet)
@cache()
async def get_self(user=Depends(get_current_user)):
    return user
