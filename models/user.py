#!/usr/bin/python3

"""
user:
    This module contains the defination of the class user.
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    User:
        A class for User object.
    """

    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
