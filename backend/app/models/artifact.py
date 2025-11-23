from sqlalchemy import Column, String, Text, Integer
from sqlalchemy.orm import relationship
from app.database import Base

class Artifact(Base):
    __tablename__ = "artifacts"

    artifactID = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    max_rarity = Column(Integer, nullable=False)
    two_set_bonus = Column(Text, nullable=False)
    four_set_bonus = Column(Text, nullable=False)
    image = Column(String, nullable=True)

    # Relationship
    domain_artifacts = relationship(
        "DomainArtifact", back_populates="artifact", cascade="all, delete-orphan"
    )
