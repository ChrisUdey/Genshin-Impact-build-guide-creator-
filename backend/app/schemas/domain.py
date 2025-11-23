from pydantic import BaseModel
from .domain_artifact import DomainArtifactResponse

class DomainResponse(BaseModel):
    id: int
    name: str
    type: str
    description: str
    location: str
    nation: str
    image: str | None
    artifacts: list[DomainArtifactResponse]  # <-- NOW CORRECT

    class Config:
        from_attributes = True
