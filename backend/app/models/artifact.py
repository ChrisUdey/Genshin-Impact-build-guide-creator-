# app/models/artifact.py
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.database import Base

class Artifact(Base):
    __tablename__ = "artifacts"

    artifactID = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    max_rarity = Column(String, nullable=False)
    two_set_bonus = Column(String, nullable=True)
    four_set_bonus = Column(String, nullable=True)
    image = Column(String, nullable=True)

    # Use string reference; do NOT import DomainArtifact here
    domain_artifacts = relationship("DomainArtifact", back_populates="artifact")
