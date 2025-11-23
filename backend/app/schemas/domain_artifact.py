from pydantic import BaseModel

class ArtifactResponse(BaseModel):
    artifactID: str
    name: str
    max_rarity: int
    two_set_bonus: str
    four_set_bonus: str
    image: str | None

    class Config:
        from_attributes = True


class DomainArtifactResponse(BaseModel):
    id: int
    artifact_id: str
    artifact: ArtifactResponse | None = None  # <-- NESTED ARTIFACT

    class Config:
        from_attributes = True
