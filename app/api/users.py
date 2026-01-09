from fastapi import APIRouter

from api.dependencies.fastapi_users_router import fastapi_users
from core.schemas.users import UserCreate, UserRead, UserUpdate

router = APIRouter(
    tags=["users"],
)

router.include_router(
    router=fastapi_users.get_register_router(
        UserRead,
        UserCreate,
    ),
)

router.include_router(
    router=fastapi_users.get_users_router(
        UserRead,
        UserCreate,
    ),
)
