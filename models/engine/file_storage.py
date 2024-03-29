#!/usr/bin/python3
"""
Serializing instances to a JSON file and
Deserializing JSON file to instances
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review


class FileStorage:
    """A storage class that serialises instances to a JSON file
    and deserialises a JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}
    __classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'Amenity': Amenity,
        'City': City,
        'Place': Place,
        'Review': Review,
    }

    def all(self):
        """A public instance method to the storage class
        Returns:
            the dictionary '__objects'
        """
        return self.__objects

    def new(self, obj):
        """A public instance method to the storage class that sets
        inside of '__objects', the 'obj' with key <obj class name>.id
        """
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        """A public instance method to the storage class that serialises
        '__objects' to the JSON file
        """
        serialised_objs = {}
        for key, value in self.__objects.items():
            serialised_objs[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='UTF-8') as json_file:
            json.dump(serialised_objs, json_file)

    def reload(self):
        """A public instance method to the storage class that deserialises
        the JSON file to '__objects' if the JSON file exists."""
        try:
            with open(
                self.__file_path, 'r', encoding='UTF-8'
            ) as json_file:
                self.__objects = json.load(json_file)
                for key, value in self.__objects.items():
                    cls = value['__class__']
                    self.all()[key] = self.__classes[cls](**value)
        except FileNotFoundError:
            pass
