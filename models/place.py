#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """

    #if getenv('HBNB_TYPE_STORAGE') == 'db':
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", backref="place",
                           cascade="all, delete-orphan")

    amenities = relationship('Amenity', secondary="place_amenity",
                             viewonly=False)
    """
    else:
    city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0

     longitude = 0.0
    """
    amenity_ids = []
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            "Returns a list of Review instances."""
            from models import storage

            all_rev = storage.all("Review").values
            place_rev = []
            for review in all_rev:
                if review.place_id == self.id:
                    place_rev.append(review)

            return place_rev

        @property
        def amenities(self):
            """Returns the list of Amenity instances."""
            from models import storage

            amenity_ids = storage.all("Amenity").values
            place_amen = []
            for amenity in amenity_ids:
                if amenity.place_id == self.id:
                    place_amen.append(amenity)

            return place_amen

        @amenities.setter
        def amenities(self, obj):
            """Handles appending an Amenity.id to the attribute amenity_ids."""
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
