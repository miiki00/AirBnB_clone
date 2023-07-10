#!/usr/bin/python3

"""
file_storage:
    This module holds the defination of the class FileStorage
    which handles the storage of objects.
"""

import json


class FileStorage:
    """
    FileStorage: handles object storage persistency

    Attributes:
        __file_path (str): path to the json file holding the objects
                           json representation.
       __objects (dict): Dictionary holding the objects.
    """

    __objects = {}
    __file_path = 'storage.json'

    def all(self):
        """
        all(self):
            Returns dictionary of the objects stored.

        Return:
            Dictionry of the the stored objects.
        """
        return (FileStorage.__objects)

    def new(self, obj):
        """
        new(self, obj):
            Inserts new object to the collection of objects.

        Args:
            obj: The object to be stored.

        Return:
            None.
        """
        FileStorage.__objects[f'{type(obj).__name__}.{obj.id}'] = obj

    def save(self):
        """
        save(self):
            Saves the objects collection dictionary in to a file
            after converting it to a json representation.

        Return:
            None.
        """
        with open(FileStorage.__file_path, 'w') as file:
            to_serialize = FileStorage.__objects.copy()
            for key in to_serialize.keys():
                to_serialize[key] = to_serialize[key].to_dict()
            file.write(json.dumps(to_serialize))

    def reload(self):
        """
        reload(self):
            Reloads the objects from the last saved file that
            that contains the json representation of the objects.
        """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                json_str = file.read()
                if len(json_str) != 0:
                    _raw = json.loads(json_str)
                    for key in _raw.keys():
                        if _raw[key]['__class__'] == 'BaseModel':
                            from models.base_model import BaseModel
                            _raw[key] = BaseModel(**_raw[key])
                        elif _raw[key]['__class__'] == 'User':
                            from models.user import User
                            _raw[key] = User(**_raw[key])
                        elif _raw[key]['__class__'] == 'State':
                            from models.state import State
                            _raw[key] = State(**_raw[key])
                        elif _raw[key]['__class__'] == 'City':
                            from models.city import City
                            _raw[key] = City(**_raw[key])
                        elif _raw[key]['__class__'] == 'Amenity':
                            from models.amenity import Amenity
                            _raw[key] = Amenity(**_raw[key])
                        elif _raw[key]['__class__'] == 'Place':
                            from models.place import Place
                            _raw[key] = Place(**_raw[key])
                        elif _raw[key]['__class__'] == 'Review':
                            from models.review import Review
                            _raw[key] = Review(**_raw[key])
                    FileStorage.__objects = _raw
        except FileNotFoundError:
            pass
