#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """It returns the dictionary __objects"""
        return FileStorage.__objects
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        name = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[name] = obj

    def save(self):
        """serializes __objects to the JSON file(path: __file_path"""
        dic = FileStorage.__objects
        objdict = {obj: dic[obj].to_dict() for obj in dic.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path) as f:
                json_obj = json.load(f)
                for dic in json_obj.values():
                    name = dic["__class__"]
                    class_name = eval(name)
                    self.new(class_name(**dic))
        except FileNotFoundError:
            return
