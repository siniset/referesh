from sqlalchemy import Column, Integer, Text, ForeignKey
from app.db import Base


class Field(Base):
    __tablename__ = "Field"
    id = Column(
        Integer,
        autoincrement=True,
        unique=True,
        primary_key=True)
    name = Column(Text, nullable=False)
    content = Column(Text, nullable=False)
    reference_id = Column(
        Integer,
        ForeignKey(
            "Reference.id",
            ondelete="CASCADE"),
        nullable=False)
