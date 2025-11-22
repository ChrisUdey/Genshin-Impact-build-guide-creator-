from pydantic import BaseModel
from typing import Optional

class ArtifactBase(BaseModel):
    artifactID: str
    name: str
    max_rarity: int
    two_set_bonus: str
    four_set_bonus: str
    image: Optional[str] = None

class ArtifactCreate(ArtifactBase):
    pass

class ArtifactResponse(ArtifactBase):
    id: int

    class Config:
        orm_mode = True
