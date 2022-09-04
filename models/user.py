#!/usr/bin/python3

from models.base_model import BaseModel

"""The class User() inherite from the BaseModel"""
class User(BaseModel):
    """Base model the add the user inform into basemodel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    