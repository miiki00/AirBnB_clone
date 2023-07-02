#!/usr/bin/python3

"""
console:
    This module is the main entry fot the console program.
"""

import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand: Class defination for object manager command interpreter.
    """

    prompt = '(hbnb) '
    classes = {
        'BaseModel': BaseModel, 'User': User, 'State': State,
        'City': City, 'Amenity': Amenity, 'Place': Place,
        'Review': Review
        }

    def emptyline(self):
        pass

    def do_EOF(self, line):
        """(Ctrl-d) EOF : Quits out the shell program."""
        print("")
        return (True)

    def help_EOF(self):
        h_msg = '(Ctrl-d) EOF : Quits out the shell program.'
        print(h_msg)

    def do_quit(self, line):
        """
        Quit : Quits out of the shell program.
        """
        return (True)

    def help_quit(self):
        h_msg = 'Quit : Quits out of the shell program.'
        print(h_msg)

    def do_create(self, line):
        if len(line) == 0:
            print('** class name missing **')
        elif line not in HBNBCommand.classes.keys():
            print('** class doesn\'t exist **')
        else:
            obj = HBNBCommand.classes[line]()
            print(obj.id)
            storage.save()

    def help_create(self):
        h_msg = """create <class> :
    Creates an instance of a <class> and prints the id of the
    instance after that it'll saves the object to storage."""
        print(h_msg)

    def do_show(self, line):
        args = HBNBCommand.arg_parser(line)
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objs = storage.all()
            obj = None
            try:
                print(objs[f"{args[0]}.{args[1]}"])
                return
            except KeyError:
                pass
            print("** no instance found **")

    def help_show(self):
        h_msg = """show <class> <object id>:
    Prints information about the object with <object id> and
    type <class>."""
        print(h_msg)

    def do_destroy(self, line):
        args = HBNBCommand.arg_parser(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            try:
                storage.all().pop(f"{args[0]}.{args[1]}")
                storage.save()
                return
            except KeyError:
                pass
            print("** no instance found **")

    def help_destroy(self):
        h_msg = """destroy <class> <object id>:
    Removes an object with <object id> and type <class>
    from the storage."""
        print(h_msg)

    def do_all(self, line):
        objs = storage.all()
        if len(line) == 0:
            for key in objs.keys():
                print(objs[key])
        elif line in HBNBCommand.classes:
            found = False
            for key in objs.keys():
                if line in key:
                    found = True
                    print(objs[key])
        else:
            print("** class doesn't exist **")

    def help_all(self):
        h_msg = """all {class} :
        Prints all the objects on the storage if issued with out
        the {class} argument. If {class} is specified prints only
        objects that are instance of {class}."""
        print(h_msg)

    def do_update(self, line):
        args = HBNBCommand.arg_parser(line)
        len_args = len(args)
        if len_args == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len_args < 2:
            print("** instance id missing **")
        elif not HBNBCommand.check_id(args[1]):
            print("** no instance found **")
        elif len_args < 3:
            print("** attribute name missing **")
        elif len_args < 4:
            print("** value missing **")
        else:
            try:
                obj = storage.all()[f"{args[0]}.{args[1]}"]
                obj_dict = obj.to_dict()
                if args[2] in obj_dict.keys():
                    arg[3] = type(obj_dict[args[2]]).__class__(args[3])
                setattr(obj, args[2], args[3])
                storage.save()
                return
            except KeyError:
                pass
            print("** no instance found **")

    def help_update(self):
        h_msg = """update <class> <object id> <attribute> <value>:
    updates or creates an attribute <attribute> with a value of <value>
    to an object type of <class> with an id <object id>."""
        print(h_msg)

    @staticmethod
    def check_id(id):
        """
        check_id: checks if an id exists in storage of objects.

        Args:
            id (str): The id to check for.

        Return:
            True if the object is found.
            else False.
        """

        objs = storage.all()
        found = False
        for key in objs.keys():
            if id == objs[key].id:
                found = True
        return (found)

    @staticmethod
    def arg_parser(line):
        """
        arg_parser: parses arguments that are passed to do_* methods
                    and return a list of arguments.

        Args:
            line (str): the line argument passed to one of the do_*
                        methods.

        Return:
            A list of string.
        """
        args = line.split()
        len_args = len(args)

        for j in range(len_args):
            if args[j][0] == '"' and args[j][-1] != '"':
                for i in range(-1, j - len_args - 1, -1):
                    if args[i][-1] == '"':
                        start = j - len_args
                        end = i + 1
                        whole = args[start:] if end == 0 else args[start:end]
                        for k in range(start, end):
                            args.pop(k)
                        for i in range(1, len(whole) * 2 - 1, 2):
                            whole.insert(i, ' ')
                        args.append(''.join(whole)[1:-1])
                        break
                break
            elif args[j][0] == '"' and args[j][-1] == '"':
                args[j] = args[j][1:-1]
                break
        return (args)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
