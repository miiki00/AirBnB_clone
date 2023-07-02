#!/usr/bin/python3

"""
console:
    This module is the main entry fot the console program.
"""

import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand: Class defination for object manager command interpreter.
    """

    prompt = '(hbnb) '

    def emptyline(self):
        pass

    def do_EOF(self, line):
        """
        (Ctrl-d) EOF : Quits out the shell program.
        """
        return (True)

    def help_EOF(self):
        h_msg = "(Ctrl-d) EOF : Quits out the shell program."
        print(h_msg)

    def do_quit(self, line):
        """
        Quit : Quits out of the shell program.
        """
        return (True)

    def help_quit(self):
        h_msg = "Quit : Quits out of the shell program."
        print(h_msg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
