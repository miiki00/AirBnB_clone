#!/usr/bin/python3
"""module: base_model
This module contains the defination of the BaseModel class.
"""


import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel: A model that all objects in this project inherit
               from. This object model contains all the common
               methods and attributes that all objects in this
               project share.

    This is a documentation for the constructor method of this Class.
    Args:
        None.
    """

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key in kwargs.keys():
                if key == "updated_at" or key == "created_at":
                    setattr(self, key, datetime.fromisoformat(kwargs[key]))
                elif key != "__class__":
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        return (f"[{type(self).__name__}] ({self.id}) <{self.__dict__}>")

    def save(self):
        """
        save: updates the the value of the instance attriubte updated_at
              to the current time.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        to_dict: return the dictionary represenation of an instance.

        Args:
            None

        Return:
            Dictionary represenation of an instance.
        """
        self_dict = self.__dict__.copy()
        self_dict["__class__"] = type(self).__name__
        self_dict["created_at"] = self_dict["created_at"].isoformat()
        self_dict["updated_at"] = self_dict["updated_at"].isoformat()
        return (self_dict)
