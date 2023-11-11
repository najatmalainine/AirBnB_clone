#!/usr/bin/python3
"""Class FileStorage"""

import json


class FileStorage:
    """serializes and deserializes JSON files"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ returns the dictionary __objects"""
        return self.__object

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f, default=lambda o: o.__dict__)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                obj_new = json.load(f)
            for key, val in obj_new.items():
                class_name, inst_id = key.split('.')
                class_instance = globals()[class_name](**val)
                self.__objects[key] = class_instance
        except FileNotFoundError:
            pass
