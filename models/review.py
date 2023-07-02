#!/usr/bin/python3

"""
review:
    contains the defination of the class Review.
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review:
        Class defination of Review objects.
    """

    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
