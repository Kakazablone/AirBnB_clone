#!/usr/bin/python3
"""
str
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

classes = {'BaseModel' : BaseModel}

storage = FileStorage()
storage.reload()
