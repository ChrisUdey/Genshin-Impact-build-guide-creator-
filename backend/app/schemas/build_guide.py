from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional


class BuildGuideCreate(BaseModel):
    character_id: int
    title: str = Field(..., min_length=5, max_length=100)
    description: str = Field(..., min_length=20, max_length=1000)


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
    uploads: List[dict] = []

    class Config:
        from_attributes = True