from sqlalchemy import Column, Integer, String, Text, Date
from ..database import Base


class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String(100), unique=True, index=True)  # Add this line!
    name = Column(String(100), nullable=False)
    title = Column(String(200))
    vision = Column(String(50))
    weapon = Column(String(50))
    gender = Column(String(20))
    nation = Column(String(50))
    affiliation = Column(String(200))
    rarity = Column(Integer)
    release = Column(Date)
    constellation = Column(String(100))
    birthday = Column(String(20))
    description = Column(Text)