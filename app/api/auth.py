from fastapi import APIRouter

from api.dependencies.backend import authentication_backend
from api.dependencies.fastapi_users_router import fastapi_users
from core.schemas.users import UserCreate, UserRead, UserUpdate

router = APIRouter(
    tags=["auth"],
)

# /login
# /logout
router.include_router(
    router=fastapi_users.get_auth_router(
        authentication_backend,
    ),
)

# /request-verify-token
# /verify
router.include_router(
    router=fastapi_users.get_verify_router(UserRead)
)