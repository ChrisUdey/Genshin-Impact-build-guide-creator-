from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class DomainArtifact(Base):
    __tablename__ = "domain_artifacts"

    id = Column(Integer, primary_key=True, index=True)

    domain_id = Column(Integer, ForeignKey("domains.id", ondelete="CASCADE"))
    artifact_id = Column(Integer, ForeignKey("artifacts.id", ondelete="CASCADE"))

    domain = relationship("Domain", back_populates="artifacts")
    artifact = relationship("Artifact", back_populates="domain_artifacts")



