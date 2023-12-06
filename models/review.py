#!/usr/bin/python3
"""Review Module"""
import models
from models.base_model import BaseModel


class Review(BaseModel):
    """ Class Review that inherits from BaseModel """
    place_id = ""
    user_id = ""
    text = ""
