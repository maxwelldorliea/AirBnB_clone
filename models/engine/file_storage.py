#!/usr/bin/env python3

"""
This is the File Storage Engine Model.
"""

import json


class FileStorage:
    """
    Represent the File Storage Engine.
    """

    __file_path = ''
    __objects = {}

    def __init__(self, file_path=None) -> None:
        """
        Initialize the File Storage.
        """
        FileStorage.__file_path = file_path
        FileStorage.__objects = {}

    def all(self):
        """
        Return all objects.
        """
        return self.__objects

    def new(self, obj) -> None:
        """
        Add new object in the into __objects.
        """
        if not obj:
            return
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj.to_dict()
        print(self.__objects)
    def save(self):
        """
        Save the __objects into file storage.
        """
        with open('file.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.__objects))

    def reload(self):
        """
        Convert json file to dictionary.
        """
        if not self.__file_path:
            return
        self.__objects = json.load(self.__file_path)
