#!/usr/bin/python3
"""IT loads the storage each time the class is called"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
