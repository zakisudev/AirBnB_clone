#!/usr/bin/python3
"""Class HBNBComand a program called console.py
"""

import cmd
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
           'State': State, 'City': City, 'Amenity': Amenity, 'Review': Review}


class HBNBCommand(cmd.Cmd):
    """ hbnb command interpreter """
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """ End of file"""
        print()
        return True

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def emptyline(self):
        """don´t execute nothing """
        pass

    def do_create(self, args):
        """ Creates a new instance """
        if not (args):
            print("** class name missing **")
        elif args not in classes:
            print("** class doesn't exist **")
        else:
            instance = eval(args)()
            instance.save()
            print(instance.id)

    def do_show(self, args):
        """ Prints str representation of an instance """
        if not (args):
            print("** class name missing **")
        else:
            args = args.split()
            if len(args) != 2:
                print("** instance id missing **")
            elif args[0] not in classes:
                print("** class doesn't exist **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id """
        args = line.split()
        if not line:
            print("** class name missing **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        sd = models.storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key in sd:
            del sd[key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """ Prints all str representation of all instances """
        split_args = args.split()
        n_list = []
        dict_json = models.storage.all()

        if not args:
            for key in dict_json:
                n_list.append(str(dict_json[key]))
            print(n_list)
        else:
            if split_args[0] in classes:
                cl_name = split_args[0]
                cl_obj = dict_json[cl_obj]
                for key in cl_obj:
                    n_list.append(str(cl_obj[key]))
                print(n_list)
            else:
                print("** class doesn't exist **")

    def do_update(self, args):
        """ Updates an instance based on the class name and id """
        args = args.split()
        sd = models.storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + '.' + args[1]
                if key in sd:
                    if len(args) > 2:
                        if len(args) > 3:
                            setattr(sd[key], args[2], args[3])
                            sd[key].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
