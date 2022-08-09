#!/usr/bin/python3
"""city inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """attributes of city class"""
    state_id = ''
    name = ''
