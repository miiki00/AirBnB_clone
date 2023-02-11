#!/usr/bin/python3
""" base_model:
This module contains the base model for all other classes
that inherites from the base class 'BaseModel'.

# Classes defined in this class:
    BaseModel:
        This class defines  base model for all other
        classes that inherites this class.
"""
import uuid
from datetime import datetime


class BaseModel:
    """BaseModel:
    This class defines base model for all other
    classes that inherites this class.

    Instance Attributes:
        id (str): uuid that is used to identifie an object.
        created_at (obj: datetime): the date and time the instance
                                    was created.
        updated_at (obj: datetime): the last date and time the instance
                                    is updated.

    This is documentation for the constructor method of this
    class:

    Args:
        No Arguments.

    Return:
        The object Created.
    """

    def __init__(self):
        # assiging id
        obj_id = uuid.uuid4()
        self.id = str(obj_id)

        # setting the time the object was created.
        current_dt = datetime.now()
        self.created_at = current_dt
        self.updated_at = current_dt
 
    def __str__(self):
        toReturn = '[{}] ({}) {}'
        return (toReturn.format(type(self).__name__, self.id, self.__dict__))

    def save(self):
        """save:
        This method updated the value of public instance attribute
        'updated_at' with the current time.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """to_dict:
        This method returns a dictionary containing all
        keys/value of __dict__ of the instance.
        """
        toReturn = self.__dict__
        toReturn['__class__'] = type(self).__name__
        toReturn['created_at'] = self.created_at.isoformat()
        toReturn['updated_at'] = self.updated_at.isoformat()

        return (toReturn)
