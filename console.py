#!/usr/bin/python3
''' This module defines the entry point of the command interpreter '''
from models.base_model import BaseModel
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
import cmd


class HBNBCommand(cmd.Cmd):
    ''' The HBNB interpreter implementation class '''
    prompt = "(hbnb) "

    classes = [
        'BaseModel', 'City', 'Amenity',
        'Place', 'Review', 'State', 'User'
    ]

    def do_help(self, arg):
        ''' To get help on a command, type help <topic>. '''
        return super().do_help(arg)

    def do_EOF(self, arg):
        ''' This function used to quit the cmd '''
        return True

    def do_quit(self, arg):
        ''' Quit command to exit the program '''
        return True

    def emptyline(self):
        ''' Do nothing on an empty line '''
        pass

    def do_create(self, arg):
        ''' Creates a new instance of BaseModel '''
        args = arg.split()
        try:
            if not arg:
                raise Exception("** class name missing **")
            elif args[0] not in self.classes:
                raise Exception("** class doesn't exist **")
            else:
                print(eval(args[0]).create())
        except Exception as e:
            print(e)

    def do_show(self, arg):
        ''' Prints the string representation of an instance '''
        args = arg.split()
        object = storage.all()
        try:
            if not args:
                raise Exception("** class name missing **")
            elif args[0] not in self.classes:
                raise Exception("** class doesn't exist **")
            elif len(args) < 2:
                raise Exception("** instance id missing **")
            elif "{}.{}".format(args[0], args[1]) not in object:
                raise Exception("** no instance found **")
            else:
                print(eval(args[0]).show(args[1].strip('"').strip("'")))
        except Exception as e:
            print(e)

    def do_destroy(self, arg):
        ''' Deletes an instance based on the class name and id '''
        args = arg.split()
        object = storage.all()
        try:
            if not args:
                raise Exception("** class name missing **")
            elif args[0] not in self.classes:
                raise Exception("** class doesn't exist **")
            elif len(args) < 2:
                raise Exception("** instance id missing **")
            elif "{}.{}".format(args[0], args[1]) not in object:
                raise Exception("** no instance found **")
            else:
                eval(args[0]).destroy(args[1].strip('"').strip("'"))
        except Exception as e:
            print(e)

    def do_all(self, arg):
        ''' Prints all stored entities based or not on the class name '''
        args = arg.split()
        obj_dict = storage.all()
        if len(args) == 0:
            print([str(obj) for obj in obj_dict.values()])
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) != 0:
            print([str(obj) for obj in eval(args[0]).all()])

    def do_update(self, arg):
        ''' Updates an instance based on the class name and id '''
        args = arg.split()

        try:
            if not args:
                raise Exception("** class name missing **")
            elif args[0] not in self.classes:
                raise Exception("** class doesn't exist **")
            elif len(args) < 2:
                raise Exception("** instance id missing **")
            elif len(args) < 3:
                raise Exception("** attribute name missing **")
            elif len(args) < 4:
                raise Exception("** value missing **")

            instance_key = f"{args[0]}.{args[1]}"

            if instance_key not in storage.all().keys():
                raise Exception("** no instance found **")

            eval(args[0]).update(*args[1:])
        except Exception as e:
            print(e)

    def default(self, line):
        ''' Handles all the method call syntax and non-command cases'''
        idxs = [line.find('.'), line.find('('), line.find(')')]
        try:
            if idxs[0] == -1 or idxs[1] < idxs[0] or idxs[2] != len(line) - 1:
                print("** inappropriate syntax **")
                return
            cls = eval(line[:idxs[0]])
            if cls.__name__ not in self.classes:
                raise Exception("** class doesn't exist **")

            mthd_name = line[idxs[0] + 1:idxs[1]]

            try:
                arg_tuple = tuple(eval(line[idxs[1]:]))
            except Exception as e:
                raise Exception("** inappropriate syntax **\n" +
                                f"[{e.__class__.__name__}]: {e}")

            tlen = len(arg_tuple)
            if mthd_name in ['all', 'count', 'create']:
                result = eval(line)
                if isinstance(result, list):
                    print([str(obj) for obj in result])
                else:
                    print(result)
            elif mthd_name in ['destroy', 'show']:
                if tlen < 1:
                    raise Exception("** instance id missing **")
                result = eval(line)
                if result is not None:
                    print(result)
            elif mthd_name == 'update':
                if tlen < 1:
                    raise Exception("** instance id missing **")
                if tlen < 2:
                    raise Exception("** attribute name missing **")
                if isinstance(arg_tuple[1], str):
                    if tlen < 3:
                        raise Exception("** value missing **")
                    cls.update(arg_tuple[0], arg_tuple[1], repr(arg_tuple[2]))
                else:
                    cls.update(arg_tuple[0], repr(arg_tuple[1]))

        except Exception as e:
            print(str(e))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
