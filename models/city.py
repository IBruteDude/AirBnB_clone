#!/usr/bin/python3
''' Module defining the City class '''
from models.base_model import BaseModel


class City(BaseModel):
    ''' Class for modeling a City entity '''
    name = ''
    state_id = ''
    def __init__(self, *args, **kwargs):
        ''' Initialiser of the City class '''
        super().__init__(**kwargs)
