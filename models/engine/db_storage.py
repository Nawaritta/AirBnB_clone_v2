#!/usr/bin/python3
"""This module defines a class to manage the New engine DBStorage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from os import getenv

class DBStorage:
    """DBStorage class for database storage"""

    __engine = None
    __session = None
