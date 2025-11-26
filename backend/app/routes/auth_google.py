from fastapi import APIRouter, HTTPException, Depends
from google.oauth2 import id_token
from google.auth.transport import requests
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import SessionLocal, get_db

from app.config import settings
from app.middleware.auth import create_access_token
from app.models.user import User
from app.schemas.user import UserBase, GoogleUserCreate

class GoogleToken(BaseModel):
    token: str

router = APIRouter(prefix="/api/auth", tags=["Auth"])

@router.post("/google")
def google_auth(data: GoogleToken):
    try:
        print("\n=== GOOGLE TOKEN RECEIVED ===")
        print(data.token[:50] + "...\n")
        idinfo = id_token.verify_oauth2_token(
            data.token, requests.Request(), settings.GOOGLE_CLIENT_ID
        )

        email = idinfo["email"]
        username = idinfo.get("name", email.split("@")[0])

        db = SessionLocal()

        # Check for existing user
        user = db.query(User).filter(User.email == email).first()

        if not user:
            user = User(
                email=email,
                username=username,
                google_id=idinfo["sub"],
                provider="google",
                role="user"
            )

            db.add(user)
            db.commit()
            db.refresh(user)

        # Issue JWT
        token = create_access_token({"id": user.id, "email": user.email})
        return {"access_token": token}

    except Exception as e:
        print("\n=== GOOGLE TOKEN ERROR ===")
        print(type(e))
        print(str(e))
        raise HTTPException(status_code=400, detail="Invalid Google token")




@router.post("/google/login", response_model=UserBase)
def google_login(data: GoogleUserCreate, db: Session = Depends(get_db)):

    # Look for existing Google user
    user = db.query(User).filter(User.email == data.email).first()

    # else, create new Google-only user
    if not user:
        user = User(
            username=data.username,
            email=data.email,
            password=None,    # Google users do not have passwords
            provider="google"
        )
        db.add(user)
        db.commit()
        db.refresh(user)

    return user