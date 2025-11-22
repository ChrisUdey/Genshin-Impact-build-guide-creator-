from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

class Artifact(Base):
    __tablename__ = "artifacts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    max_rarity = Column(Integer, nullable=False)
    two_set_bonus = Column(String, nullable=False)
    four_set_bonus = Column(String, nullable=False)
    image = Column(String, nullable=True)

    domain_artifacts = relationship("DomainArtifact", back_populates="artifact")
