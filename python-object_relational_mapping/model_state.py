#!/usr/bin/python3

"""Model state"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    """Class State"""

    __tablename__ = "states"
    id = Column(
        Integer, 
        primary_key=True, 
        autoincrement=True, 
        unique=True, 
        nullable=False
    )
    name = Column(String(128), nullable=False)
