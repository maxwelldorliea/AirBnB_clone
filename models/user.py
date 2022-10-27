#!/bin/python3

"""
This is the User Module.
"""
from models.base_model import BaseModel

class User(BaseModel):
    """
    This class represent all users.
    """
    first_name : str = ''
    last_name : str = ''
    email : str = ''
    password : str = ''
