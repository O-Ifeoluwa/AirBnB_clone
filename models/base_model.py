#!/usr/bin/python3
"""Base module"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """BaseModel defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """initializes the attributes of BaseModel"""

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == '__class__':
                    continue
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """string representation of the object"""
        return "{[]} {[]} {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance `updated_at`
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()

        return my_dict
