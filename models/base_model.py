#!/usr/bin/env python3
''' Module defining the BaseModel class for other classes '''
import sys
import os
from datetime import datetime
from uuid import uuid4
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models import storage

class BaseModel:
    ''' The base model class with functionality for other entity classes '''
    __no_instances = 0

    def __init__(self, *args, **kwargs):
        ''' Initialise the base model object id '''
        self.created_at = datetime.now()
        self.id = str(uuid4())
        self.updated_at = datetime.now()
        storage.new(self)

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        obj_dict['__class__'] = type(self).__name__
        return obj_dict

    def __str__(self):
        return '[{}] ({}) {}'.format(
            type(self).__name__, self.id, self.__dict__
        )


if __name__ == '__main__':
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    # print("--------\n{}\n--------".format(type(my_model).__name__))
    print(my_model)
    print()
    my_model.save()
    print()
    print(my_model)
    print()
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print()
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(
            key, type(my_model_json[key]), my_model_json[key])
        )
