#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from datetime import datetime
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    if storage_type == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
         name = ""
         created_at = ""

        @property
        def cities(self):
            """ Returns the list of City instances in the current state """
            city_list = []
            for city in storage.all("City").values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
