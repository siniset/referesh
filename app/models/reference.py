from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from app.db import Base


class Reference(Base):
    __tablename__ = "Reference"
    id = Column(
        Integer,
        autoincrement=True,
        unique=True,
        primary_key=True)
    name = Column(Text, nullable=False)
    type = Column(Text, nullable=False)
    created_at = Column(
        DateTime(
            timezone=True),
        server_default=func.now())
    project_id = Column(
        Integer,
        ForeignKey(
            "Project.id",
            ondelete="CASCADE"),
        nullable=False)
    fields = relationship("Field")
