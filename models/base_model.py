#!/usr/bin/python3
import uuid
from datetime import datetime
import models

"""Class BaseModel is the base Model for all the class"""


class BaseModel():
    """Class that defines the BaseModel"""
    def __init__(self, *args, **kwargs):
        """
        it instanciate the class BaseModel

        Args:
            *args: is unused.
            **kwargs(dict): key/value pairs of attributes.
        """

        """
            When every a new class is created these are the items that will be
            created along with the class be default
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        """It update the class"""
        delim = "%Y-%m-%dT%H:%M:%S.%f"
        if (len(kwargs) != 0):
            for key in kwargs:
                if (key == "created_at"):
                    self.__dict__[key] = datetime.strptime(kwargs[key], delim)
                elif (key == "updated_at"):
                    self.__dict__[key] == datetime.strptime(kwargs[key], delim)
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            models.storage.new(self)

    def __str__(self):
        """
        should print: [<class name>] (<self.id>) <self.__dict__>
        when printing the class.
        """
        name = self.__class__.__name__
        return ("[{}] ({}) {}".format(name, self.id, self.__dict__))

    def save(self):
        """Update the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """creates a dictionary of BaseModel"""
        self_dictionary = dict(self.__dict__)
        self_dictionary['__class__'] = self.__class__.__name__
        self_dictionary['created_at'] = datetime.isoformat(self.created_at)
        self_dictionary['updated_at'] = datetime.isoformat(self.updated_at)
        return self_dictionary
