#!/usr/bin/python3

"""
amenity:
    contains defination of the class Amenity.
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity:
        Class defination for Amenity objects.
    """

    name = ''

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
