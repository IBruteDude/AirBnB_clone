#!/usr/bin/python3
from models.base_model import BaseModel
import cmd

class HBNBCommand(cmd.Cmd):

    prompt ="(hbnb) "

    def do_EOF(self, arg):
        ''' This function used to quit the cmd '''
        return True

    def do_quit(self, arg):
        ''' This function used to quit the cmd '''
        return True

    def emptyline(self):
        ''' Do nothing on an empty line '''
        pass

    def do_create(self, arg):
        ''' Creates a new instance of BaseModel '''
        if not arg:
            print("** class name missing **")
        elif arg == 'BaseModel':
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        ''' Prints the string representation of an instance based on the class name and id '''
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ['BaseModel']:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")


    def do_destroy(self):
        ''' Deletes an instance based on the class name and id '''

    def do_all(self):
        ''' Prints all string representation of all instances based or not on the class name '''

    def do_update(self):
        ''' Updates an instance based on the class name and id '''

if __name__ == '__main__':
    HBNBCommand().cmdloop()