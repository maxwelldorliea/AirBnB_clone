#!/usr/bin/python3
"""This is the Base Model For All Models."""

from datetime import datetime as dtime
from uuid import uuid4
import models


class BaseModel:
    """This Model Implement All common attribute for other model."""

    def __init__(self, *arg, **kwarg) -> None:
        """Initialize the BaseModel."""
        if kwarg:
            attr = kwarg.copy()
            del attr['__class__']
            ctd_at = attr['created_at']
            attr['created_at'] = dtime.strptime(ctd_at, '%Y-%m-%dT%H:%M:%S.%f')
            upd_at = attr['updated_at']
            attr['updated_at'] = dtime.strptime(upd_at, '%Y-%m-%dT%H:%M:%S.%f')

            for k in attr:
                setattr(self, k, attr[k])
        else:
            self.id = str(uuid4())
            self.created_at = dtime.now()
            self.updated_at = dtime.now()
            models.storage.new(self)

    def __str__(self) -> str:
        """Return the string representation of BaseModel."""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self) -> None:
        """Update the BaseModel Data."""
        self.updated_at = dtime.now()
        models.storage.save()

    def to_dict(self) -> dict:
        """Return the dictionary representation of BaseModel."""
        attr = self.__dict__.copy()
        attr['__class__'] = self.__class__.__name__
        if not type(attr['created_at']) is str:
            attr['created_at'] = attr['created_at'].isoformat()
        if not type(attr['updated_at']) is str:
            attr['updated_at'] = attr['updated_at'].isoformat()
        return attr
