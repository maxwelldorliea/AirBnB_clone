#!/bin/python3

"""This is the Review Module."""

from models.base_model import BaseModel


class Review(BaseModel):
    """This class represent all Reviews."""

    place_id: str = ''
    user_id: str = ''
    text: str = ''
