#!/usr/bin/python3
"""This is the Amenity Module."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """This class represent all Amenity."""

    name: str = ''
