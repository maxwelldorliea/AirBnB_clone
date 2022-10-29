#!/bin/python3

"""This is the Place Module."""

from models.base_model import BaseModel


class Place(BaseModel):
    """This class represent all place."""

    city_id: str = ''
    user_id: str = ''
    name: str = ''
    description: str = ''
    number_room: int = 0
    number_bathrooms: int = 0
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_ids: list = []
