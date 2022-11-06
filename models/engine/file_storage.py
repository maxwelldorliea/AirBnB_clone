#!/usr/bin/python3
"""This is the File Storage Engine Model."""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Represent the File Storage Engine."""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Return all objects."""
        return self.__objects

    def new(self, obj) -> None:
        """Add new object in the into __objects."""
        if not obj:
            return
        attr = obj.to_dict()
        key = attr['__class__'] + '.' + attr['id']
        self.__objects[key] = obj

    def save(self):
        """Save the __objects into file storage."""
        objs = {}
        for key in self.__objects:
            objs[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(objs, f, indent=8)

    def reload(self):
        """Convert json file to dictionary."""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                objs = json.loads(f.read())
                for key, obj in objs.items():
                    if key not in self.__objects:
                        name = obj['__class__']
                        base = eval(f"{name}(**obj)")
                        self.new(base)
        except Exception:
            pass
