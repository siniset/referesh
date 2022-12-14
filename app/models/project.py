from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship
from app.db import Base


class Project(Base):
    __tablename__ = "Project"
    id = Column(
        Integer,
        autoincrement=True,
        unique=True,
        primary_key=True)
    name = Column(Text, nullable=False)
    references = relationship("Reference")