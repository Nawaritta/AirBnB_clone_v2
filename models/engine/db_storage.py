#!/usr/bin/python3
"""This module defines a class to manage the New engine DBStorage"""
from models.base_model import BaseModel, Base
from models import place
from models import user, state, amenity, city, review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """DBStorage class for database storage"""

    __engine = None
    __session = None

    def __init__(self):
        """Create the engine (self.__engine)"""
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        db_url = 'mysql+mysqldb://{}:{}@{}/{}'.format(user, pwd, host, db)

        self.__engine = create_engine(db_url, pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session"""
        from models import storage
        if cls:
            classes = [cls]
        else:
            classes = [user.User, state.State, city.City,
                       amenity.Amenity, place.Place, review.Review]
        objects = {}
        for cls in classes:
            for obj in self.__session.query(cls).all():
                key = '{}.{}'.format(type(obj).__name__, obj.id)
                objects[key] = obj

        return objects

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj:
            self.__session.delete(obj)
        if not self.__session:
            self.reload()

    def reload(self):
        """Create all tables in the database (feature of SQLAlchemy)"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False))


    def close(self):
        """to display HBNB data using Flask"""
        self.__session.__class__.close(self.__session)
        self.reload()
