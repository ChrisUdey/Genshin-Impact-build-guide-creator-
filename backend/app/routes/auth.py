from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from ..middleware.auth import authenticate_user, create_access_token

router = APIRouter(prefix="/api/auth", tags=["authentication"])


class LoginRequest(BaseModel):
    email: str
    password: str


@router.post("/login")
async def login(credentials: LoginRequest):
    user = authenticate_user(credentials.email, credentials.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    token = create_access_token({"id": user["id"], "email": user["email"]})
    return {"token": token, "user": user}