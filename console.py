#!/usr/bin/python3
"""Class Cmd"""
import cmd


class HBNBCommand(cmd.Cmd):
    """entry point of the command interpreter"""
    prompt = "(hbnb) "
    classes = {'BaseModel': BaseModel, 'User': User, 'City': City,
               'Place': Place, 'Amenity': Amenity, 'Review': Review,
               'State': State}

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

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = self.classes[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objects = storage.all()
            if key not in all_objects:
                print("** no instance found **")
            else:
                print(all_objects[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objects = storage.all()
            if key not in all_objects:
                print("** no instance found **")
            else:
                del all_objects[key]
                storage.save()

    def do_all(self, arg):
        """ Method to print all instances """
        if len(arg) == 0:
            print([str(a) for a in storage.all().values()])
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(a) for b, a in storage.all().items() if arg in b])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
