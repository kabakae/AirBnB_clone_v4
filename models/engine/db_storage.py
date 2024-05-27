#!/usr/bin/python3
"""
Contains the DBStorage class
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": Base, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}

class DBStorage:
    """Interacts with the MySQL database"""

    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        self.__engine = create_engine('mysql+mysqldb://<user>:<password>@<host>/<database>')

    def all(self, cls=None):
        """Query on the current database session"""
        if cls:
            objects = self.__session.query(cls).all()
        else:
            objects = []
            for class_name in classes.values():
                objects.extend(self.__session.query(class_name).all())
        return {f"{obj.__class__.__name__}.{obj.id}": obj for obj in objects}

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

    def reload(self):
        """Reload data from the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Remove the session"""
        self.__session.remove()

