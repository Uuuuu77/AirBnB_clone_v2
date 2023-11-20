#!/usr/bin/python3
"""
    Module for database storage.
"""
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """ Database storage engine """
    __engine = None
    __session = None

    def __init__(self):
        """ Initializing my class """
        usr = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}:3306/{}"
                                      .format(usr, pwd, host,
                                              db), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_off(self.__engine)

    def all(self, cls=None):
        """ Queries on current database session depending on class name """
        cls_lst = [State, City, User, Place, Review, Amenity]

        dtb = {}
        if cls:
            for obj in self.__session.query(cls).all():
                key = f"{obj.__class__.__name__}.{obj.id}"
                dtb[key] = obj
        else:
            for cl in cls_lst:
                for obj in self.__session.query(cl).all():
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    dtb[key] = obj
        return dtb

    def new(self, obj):
        """ Adds object to current database session """
        self.__session.add(obj)

    def save(self):
        """ Commits all changes to current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes from current database session """
        if obj:
            self.__session.delets(obj)

    def reload(self):
        """ Creates all table in database """
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess)
        self.__session = Session()

    def close(self):
        """ Closing of the session """
        self.__session.close()
