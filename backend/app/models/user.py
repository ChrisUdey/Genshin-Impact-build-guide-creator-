from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=True)  # for standard login
    role = Column(String, default="user")

    # Google login support
    google_id = Column(String, nullable=True)
    provider = Column(String, nullable=True, default="local")
