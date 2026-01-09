from fastapi_users.authentication import BearerTransport
import secrets
bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")