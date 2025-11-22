from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from ..database import Base



class Domain(Base):
    __tablename__ = "domains"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    location = Column(String, nullable=False)
    nation = Column(String, nullable=False)
    picture_path = Column(String, nullable=True)

    # NEW
    artifacts = relationship("DomainArtifact", back_populates="domain", cascade="all, delete-orphan")

