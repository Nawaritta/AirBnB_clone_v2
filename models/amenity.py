#!/usr/bin/python3
""" State Module for HBNB project"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String
from sqlalchemy.orm import relationship
from os import getenv


class Amenity(BaseModel, Base):
    """Class Amenity """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        from models.place import place_amenity
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place', secondary=place_amenity,
        back_populates='amenities')

    else:
        name = ""
