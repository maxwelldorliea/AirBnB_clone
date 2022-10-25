#!/usr/bin/env python3

"""
This is the Base Model Of All Models.
"""
import uuid
import datetime
from models import storage

class BaseModel:
    """
    Represent the Base Model.
    """

    def __init__(self, *args, **kwargs) -> None:
        """
        Initialized the Base Model.
        """
        if kwargs:
            kpairs = kwargs.copy()
            del kpairs['__class__']
            for k in kpairs:
                setattr(self, k, kpairs[k])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self) -> str:
        """
        Return string representation Base Model.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self) -> None:
        """
        Update the Base Model.
        """
        self.updated_at = datetime.datetime.now()
        #storage.save()
    
    def to_dict(self):
        """
        Return the dictionary representation Of Base Model
        """
        attr = self.__dict__
        attr['__class__'] = self.__class__.__name__
        attr['updated_at'] = attr['updated_at'].isoformat()
        attr['created_at'] = attr['created_at'].isoformat()
        return attr
