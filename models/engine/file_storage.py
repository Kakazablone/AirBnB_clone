#!/usr/bin/python3
"""File storage Module"""
import json


class FileStorage:
    """Class that defines the storage methods. It has two
    private global attributes;
    file_path (str): path to the JSON file
    objects (dict): stores all objects by class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all instances, in dictionary format,
        that have been stored previously"""
        return self.__objects

    def new(self, obj):
        """Adds a new object to the dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Dump the instance in Json format"""
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            obj_dict = {}
            for key, value in self.__objects.items():
                obj_dict[key] = value.to_dict()
            json.dump(obj_dict, f, ensure_ascii=False, indent=4)

    def reload(self):
        """Reloads the JSON instances that had
        been saved previously"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    if class_name in self.classes:
                        obj_class = self.classes[class_name]
                        obj_instance = obj_class(**value)
                        self.__objects[key] = obj_instance
                    else:
                        print(f"Warning: Class {class_name} not found")
        except FileNotFoundError:
            pass

    @property
    def classes(self):
        """This returns a dictionary of valid classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes
