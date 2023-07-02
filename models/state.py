#!/usr/bin/python3

"""
state:
    contains the defination of the class State.
"""


from models.base_model import BaseModel


class State(BaseModel):
    """
    State:
        a class defination for State object.
    """

    name = ''

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
