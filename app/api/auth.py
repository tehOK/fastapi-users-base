from fastapi import APIRouter

from api.dependencies.backend import authentication_backend
from api.dependencies.fastapi_users_router import fastapi_users

router = APIRouter(
    tags=["auth"],
)

router.include_router(
    router=fastapi_users.get_auth_router(
        authentication_backend,
    ),
)
