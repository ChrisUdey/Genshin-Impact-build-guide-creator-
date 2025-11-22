from typing import List, Optional
from pydantic import BaseModel

from app.schemas.domain_artifact import DomainArtifactResponse


class DomainBase(BaseModel):
    name: str
    type: str
    description: str
    location: str
    nation: str
    picture_path: Optional[str] = None

class DomainCreate(DomainBase):
    pass

class DomainResponse(DomainBase):
    id: int
    artifacts: List[DomainArtifactResponse] = []

    class Config:
        orm_mode = True
