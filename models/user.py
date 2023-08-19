#!/usr/bin/python3
''' Module defining the User class '''
from models.base_model import BaseModel


class User(BaseModel):
    ''' Class for modeling a User entity '''
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        ''' Initialiser of the State class '''
        super().__init__(**kwargs)
