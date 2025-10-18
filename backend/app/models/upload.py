from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base


class Upload(Base):
    __tablename__ = "uploads"

    id = Column(Integer, primary_key=True, index=True)
    build_guide_id = Column(Integer, ForeignKey("build_guides.id"), nullable=False)
    image_path = Column(String(500), nullable=False)
    caption = Column(String(200), nullable=False)
    uploaded_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    build_guide = relationship("BuildGuide", back_populates="uploads")