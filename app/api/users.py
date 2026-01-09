from fastapi import APIRouter

from api.dependencies.fastapi_users_router import fastapi_users
from core.schemas.users import UserCreate, UserRead, UserUpdate

router = APIRouter(
    tags=["users"],
)

# /register
router.include_router(
    router=fastapi_users.get_register_router(
        UserRead,
        UserCreate,
    ),
)

# /me
# /{id}
router.include_router(
    router=fastapi_users.get_users_router(
        UserRead,
        UserCreate,
    ),
)

# /forgot-password
# /reset-password
router.include_router(
    router=fastapi_users.get_reset_password_router()
)
