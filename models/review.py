#!/usr/bin/python3

from models.base_model import BaseModel

"""The class Review() inherite from the BaseModel"""
class Review(BaseModel):
    """It add review information to BaseModel"""
    place_id = ""
    user_id = ""
    text = ""