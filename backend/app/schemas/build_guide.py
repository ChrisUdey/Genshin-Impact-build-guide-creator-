from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import List, Optional


class BuildGuideCreate(BaseModel):
    character_id: int
    title: str = Field(..., min_length=5, max_length=100)
    description: str = Field(..., min_length=20, max_length=1000)


class BuildGuideFormCreate(BaseModel):
    """Schema for form submission with server-side validation"""
    username: str = Field(..., min_length=4, max_length=20)
    character_name: str = Field(..., min_length=1, max_length=100)
    title: str = Field(..., min_length=4, max_length=30)
    description: str = Field(..., min_length=10, max_length=350)

    @validator('username')
    def username_alphanumeric(cls, v):
        """Username must be alphanumeric (underscores and hyphens allowed)"""
        if not v.replace('_', '').replace('-', '').isalnum():
            raise ValueError('Username must be alphanumeric (underscores and hyphens allowed)')
        return v.strip()

    @validator('title', 'description')
    def not_empty_whitespace(cls, v):
        """Fields cannot be empty or whitespace only"""
        if not v.strip():
            raise ValueError('Cannot be empty or whitespace only')
        return v.strip()


class UploadCreate(BaseModel):
    caption: str = Field(..., min_length=5, max_length=200)


class UploadResponse(BaseModel):
    id: int
    image_path: str
    caption: str
    uploaded_at: datetime

    class Config:
        from_attributes = True


class BuildGuideResponse(BaseModel):
    id: int
    username: str
    character_id: int
    character_name: Optional[str]
    title: str
    description: str
    picture_path: Optional[str]
    created_at: str
    status: Optional[str] = "pending"
    uploads: List[dict] = []

    class Config:
        from_attributes = True