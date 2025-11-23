from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.database import Base

class Domain(Base):
    __tablename__ = "domains"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    type = Column(String, unique=False, nullable=False)
    description = Column(Text, nullable=True)
    location = Column(Text, nullable=True)
    nation = Column(Text, nullable=True)
    image = Column(Text, nullable=True)

    # Relationship
    artifacts = relationship(
        "DomainArtifact", back_populates="domain", cascade="all, delete-orphan"
    )
