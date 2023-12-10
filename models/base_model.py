#!/usr/bin/python3
"""BaseModel Module that all other classes will inherit from"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """The defined BaseModel class"""
    def __init__(self, *args, **kwargs):
        """Initializes an instance of the class in two ways;
        1. If the user provides kwargs &
        2. Where no kwargs are provided.
        ATTRIBUTES: these include id (UUID), created at and
        updated at"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at':
                    value = datetime.fromisoformat(value)
                    self.created_at = value
                elif key == 'updated_at':
                    value = datetime.fromisoformat(value)
                    self.updated_at = value
                elif key == 'id':
                    self.id = str(value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def save(self):
        """Saves an any created instance by first ensuring
        that time is current and then uses the storage method
        to store the instance in JSON format"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Defines storage format of dictionary"""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = type(self).__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()

        return dictionary

    def __str__(self):
        """The string representation of any instance"""
        class_name = type(self).__name__

        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
