#!/usr/bin/python3
"""This is the City Module."""

from models.base_model import BaseModel


class City(BaseModel):
    """This class represent all cities."""

    state_id: str = ''
    name: str = ''
