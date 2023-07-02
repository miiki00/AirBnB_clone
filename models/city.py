#!/usr/bin/python3

"""
city:
    contains the defination of the class City.
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    City:
        Class defination for City objects.
    """

    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
