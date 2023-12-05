#!/usr/bin/python3
"""Command interpreter adapted from Cmd Module"""
import models
import cmd


class HBNBCommand(cmd.Cmd):
    """The command line interpreter"""

    prompt = '(hbnb) '

    def do_EOF(self, line):
        """ Exit at EOF"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the interpreter"""
        return True

    def emptyline(self):
        """Do nothing if line is empty"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
