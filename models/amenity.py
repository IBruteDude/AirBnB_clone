#!/usr/bin/python3
''' Module defining the Amenity class '''
from models.base_model import BaseModel


class Amenity(BaseModel):
    ''' Class for modeling a Amenity entity '''
    name = ''

    def __init__(self, *args, **kwargs):
        ''' Initialiser of the Amenity class '''
        super().__init__(**kwargs)
