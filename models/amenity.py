#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from models.place import place_amenity
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """this is the class 4 Amenity
    attributes:
        name: input name
    """
    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
