#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
        else:
            attr = {k: v for k, v in kwargs.items() if k != '__class__'}
            if 'id' not in attr:
                self.id = str(uuid.uuid4())
            if 'created_at' not in attr:
                self.created_at = self.updated_at = datetime.now()
            for key, val in attr.items():
                if key in ['created_at', 'updated_at']:
                    dt_obj = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, dt_obj)
                else:
                    setattr(self, key, val)

    def __str__(self):
        """Returns a string representation of the instance"""
        dtn = dict(self.__dict__)
        if "_sa_instance_state" in dtn:
            del dtn["_sa_instance_state"]
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                      dtn))

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dt = {}
        dt["__class__"] = self.__class__.__name__
        for key, val in self.__dict__.items():
            if type(val) == datetime:
                dt[key] = val.isoformat()
            else:
                dt[key] = val
        if "_sa_instance_state" in dt:
            del dt["_sa_instance_state"]
        return dt

    def delete(self):
        """ Deletes current instance from storage """
        from models import storage
        storage.delete(self)
