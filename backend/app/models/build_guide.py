from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base


class BuildGuide(Base):
    __tablename__ = "build_guides"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    character_id = Column(Integer, ForeignKey("characters.id"), nullable=False)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    picture_path = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    character = relationship("Character")
    uploads = relationship("Upload", back_populates="build_guide", cascade="all, delete-orphan")