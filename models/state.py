#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from datetime import datetime
import models

class State(BaseModel):
    """ State class """
    name = ""
    created_at = ""
