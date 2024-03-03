#!/usr/bin/python3
"""This module defines a class User"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from models.place import Place
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """ this is the class 4 user"""
    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="user")
