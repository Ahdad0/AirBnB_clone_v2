#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
import models
from models.review import Review
from os import getenv
from sqlalchemy.orm import relationship


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128))
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                               backref="place")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """returns list of reviews.id """
            v = models.storage.all()
            lis = []
            res = []
            for key in v:
                rev = key.replace('.', ' ')
                rev = shlex.split(rev)
                if (rev[0] == 'Review'):
                    lis.append(v[key])
            for elem in lis:
                if (elem.place_id == self.id):
                    res.append(elem)
            return (res)

        @property
        def amenities(self):
            """returns list of amenity"""
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """appends amenity ids"""
            if type(obj) == Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
