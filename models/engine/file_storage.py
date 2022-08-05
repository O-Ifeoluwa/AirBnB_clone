#!/usr/bin/python3
"""serialization and deserialization"""
import json


class FileStorage():
    """
    serializes instances to JSON file and
    deserializes JSON files to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        """initializing method"""
        super().__init__()

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dumps(FileStorage.__objects, f, default=str)

    def reload(self):
        """
        deserializes the JSON file to __objects
        - only if the JSON file exists
        """
        try:
            with open(FileStorage,__file_path, 'r', encoding='utf-8') as f:
                FileStorage.__objects = json.load(f)
        except Exception:
            print(Exception)
