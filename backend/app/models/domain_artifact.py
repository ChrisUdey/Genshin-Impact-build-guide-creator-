from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class DomainArtifact(Base):
    __tablename__ = "domain_artifacts"

    id = Column(Integer, primary_key=True, index=True)
    domain_id = Column(Integer, ForeignKey("domains.id", ondelete="CASCADE"), nullable=False)
    artifact_id = Column(String, ForeignKey("artifacts.artifactID", ondelete="CASCADE"), nullable=False)

    domain = relationship("Domain", back_populates="artifacts")
    artifact = relationship("Artifact", back_populates="domain_artifacts")
