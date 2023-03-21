#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid

from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime


# Declarative base class - enables mapping of tables
Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        # self.id = str(uuid.uuid4())
        # self.created_at = datetime.now()
        # self.updated_at = datetime.now()

        # if kwargs:
        #     if kwargs.get("updated_at"):
        #         kwargs["updated_at"] = datetime.strptime(
        #             kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
        #         )
        #     if kwargs.get("created_at"):
        #         kwargs["created_at"] = datetime.strptime(
        #             kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
        #         )
        #     if kwargs.get("__class__"):
        #         del kwargs["__class__"]
        #     self.__dict__.update(kwargs)
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split(".")[-1]).split("'")[0]
        return "[{}] ({}) {}".format(cls, self.id, self.__dict__)

    def save(self):
        from models import storage

        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()

        if dictionary.get("_sa_instance_state"):
            del dictionary["_sa_instance_state"]
        return dictionary

    def delete(self):
        """Deletes the current instance from storage `models.storage`"""
        from models import storage

        storage.delete(self)
