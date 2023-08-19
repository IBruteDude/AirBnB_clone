#!/usr/bin/python3
''' Module defining the BaseModel class for other classes '''
import sys
import os
from datetime import datetime
from uuid import uuid4
from models import storage
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class BaseModel:
    ''' The base model class with functionality for other entity classes '''

    def __init__(self, *args, **kwargs):
        ''' Initialise the base model object id '''
        if len(kwargs) == 0:
            self.created_at = datetime.now()
            self.id = str(uuid4())
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in zip(kwargs.keys(), kwargs.values()):
                if key != '__class__':
                    setattr(self, key, value)
            if hasattr(self, 'created_at'):
                self.created_at = datetime.fromisoformat(self.created_at)
            if hasattr(self, 'updated_at'):
                self.updated_at = datetime.fromisoformat(self.updated_at)

    def save(self):
        ''' Saves the timestamp of updating the instance '''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        ''' Converts the instance into a dict representation '''
        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        obj_dict['__class__'] = type(self).__name__
        return obj_dict

    def __str__(self):
        ''' String representation of the instance '''
        return '[{}] ({}) {}'.format(
            type(self).__name__, self.id, self.__dict__
        )

    @classmethod
    def all(cls):
        all_found = []
        for key, value in storage.all().items():
            if key[:key.find('.')] == cls.__name__:
                all_found.append(value)
        return all_found

    @classmethod
    def count(cls):
        return len(cls.all())

    @classmethod
    def create(cls):
        new_obj = cls()
        storage.save()
        return new_obj.id

    @classmethod
    def show(cls, uuid):
        objs_list = cls.all()
        for obj in objs_list:
            if obj.id == uuid:
                return obj
        print("** no instance found **")

    @classmethod
    def destroy(cls, uuid):
        objs_dict = storage.all()
        key = f'{cls.__name__}.{uuid}'
        if key in objs_dict.keys():
            del objs_dict[key]
        else:
            print("** no instance found **")
        storage.save()

    @classmethod
    def update(cls, *args):
        uuid = args[0]
        obj = cls.show(uuid)
        if obj is not None:
            if len(args) == 2:
                dict_repr = dict(eval(args[1]))
                for key, value in dict_repr.items():
                    if key not in ["id", "created_at", "updated_at"]:
                        setattr(obj, key, value)
                obj.save()
            else:
                attr_name, attr_value = args[1], eval(args[2])
                if attr_name not in ["id", "created_at", "updated_at"]:
                    setattr(obj, attr_name, attr_value)
                obj.save()


if __name__ == '__main__':
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89

    print(my_model.id)
    # print("--------\n{}\n--------".format(type(my_model).__name__))
    print(my_model)
    print()
    my_model.save()
    print()
    print(my_model)
    print()
    print()
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print()
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(
            key, type(my_model_json[key]), my_model_json[key])
        )
