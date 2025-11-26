from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from ..database import get_db
from ..middleware.auth import authenticate_user, create_access_token
from ..models.user import User
from ..schemas.user import UserCreate, UserBase

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


@router.post("/register", response_model=UserBase)
def register(user: UserCreate, db: Session = Depends(get_db)):

    # Check if email already exists
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(400, "Email already registered")

    new_user = User(
        username=user.username,
        email=user.email,
        password=user.password,  # plain text
        provider="local"
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user