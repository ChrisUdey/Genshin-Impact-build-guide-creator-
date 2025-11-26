from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    id: int
    username: str
    email: str
    provider: str

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class GoogleUserCreate(BaseModel):
    email: str
    username: str
