#!/usr/bin/python3
"""class inherits from BaseModel"""
from base_model import BaseModel


class User(BaseModel):
    """User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
