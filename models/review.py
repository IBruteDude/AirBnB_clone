#!/usr/bin/python3
''' Module defining the Review class '''
from models.base_model import BaseModel


class Review(BaseModel):
    ''' Class for modeling a Review entity '''
    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        ''' Initialiser of the Review class '''
        super().__init__(**kwargs)
