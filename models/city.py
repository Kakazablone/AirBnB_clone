#!/usr/bin/env python3
"""City Module """
import models
from models.base_model import BaseModel


class City(BaseModel):
    """ Class City that inherits from BaseModel """
    state_id = ""
    name = ""
