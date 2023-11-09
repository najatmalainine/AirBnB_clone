#!/usr/bin/python3
"""Class Cmd"""
import cmd


class HBNBCommand(cmd.Cmd):
    """entry point of the command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, arg):
        """Handles EOF to exit the program"""
        print()
        exit()

    def emptyline(self):
        """Called when an empty line + ENTER is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
