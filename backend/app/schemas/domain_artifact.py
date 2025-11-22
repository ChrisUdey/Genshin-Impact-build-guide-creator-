from pydantic import BaseModel

from app.schemas.artifact import ArtifactResponse


class DomainArtifactBase(BaseModel):
    domain_id: int
    artifact_id: int

class DomainArtifactCreate(DomainArtifactBase):
    pass

class DomainArtifactResponse(DomainArtifactBase):
    id: int
    artifact: ArtifactResponse  # include artifact details if needed

    class Config:
        orm_mode = True
