#!/usr/bin/python3
"""Command interpreter adapted from Cmd Module"""
import models
import cmd
import shlex
from models import storage
import re
import json


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

    def do_create(self, line):
        """Creates a new instance of BM, saves to JSON and prints the id """
        if not line:
            print("** class name missing **")
        elif line not in storage.classes:
            print("** class doesn't exist **")
        else:
            result = storage.classes[line]()
            models.storage.save()
            print(result.id)

    def do_show(self, line):
        """Prints string representation of instance based on name and id """
        line = shlex.split(line)
        if len(line) == 0:
            print("** class name missing **")
        elif line[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(line) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(line[0], line[1])
            temp_dict = models.storage.all()
            if key in temp_dict:
                print(temp_dict[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Destroys an instance based on class name and id & save to JSON"""
        line = shlex.split(line)
        if len(line) == 0:
            print("** class name missing **")
        elif line[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(line) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(line[0], line[1])
            temp_dict = models.storage.all()
            if key in temp_dict:
                del temp_dict[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Print all instances of a class (or all intances if no class)"""
        line = shlex.split(line)
        temp_dict = models.storage.all()
        object_list = []
        if len(line) == 0:
            for key, value in temp_dict.items():
                object_list.append(str(value))
            print(object_list)
        elif line[0] not in storage.classes:
            print("** class doesn't exist **")
        else:
            for key, value in temp_dict.items():
                if line[0] in key:
                    object_list.append(str(value))
            print(object_list)

    def do_update(self, line):
        """Update instance based on class name & id (Attribute)& save2  JSON"""
        line = shlex.split(line)
        if len(line) == 0:
            print("** class name missing **")
        elif line[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(line) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(line[0], line[1])
            temp_dict = models.storage.all()
            if key not in temp_dict:
                print("** no instance found **")
            elif len(line) == 2:
                print("** attribute name missing **")
            elif len(line) == 3:
                print("** value missing **")
            else:
                value = temp_dict.get(key)
                setattr(value, line[2], line[3])
                models.storage.save()

    def default(self, line):
        """Preprocess the command before calling the do_* method."""
        parts = line.split('.')
        if len(parts) == 2:
            class_name, action_with_args = (part.strip() for part in parts)

            if class_name in storage.classes:
                match = re.match(r'(\w+)\(([^,]*)(?:,(.*))?\)',
                                 action_with_args)
                if match and match.group(1) in ['create', 'count', 'show',
                                                'destroy', 'update', 'all']:
                    action, object_id, args = match.groups()
                    object_id = object_id.strip() if object_id else ''
                    args = args.strip() if args else ''

                    # Check if the argument is a dictionary
                    if '{' in args and '}' in args:
                        # Replace single quotes with double quotes-dictionary
                        args = args.replace("'", "\"")

                        # Safely parse the dictionary using json.loads
                        try:
                            arg_dict = json.loads(args)
                            if isinstance(arg_dict, dict):
                                # Extract key-value pairs from the dictionary
                                key_value_pairs = arg_dict.items()
                                # Iterate over key-value pairs & call update
                                saved_list = (["[[{}] [{}] [{}] [{}] [{}]]"
                                              .format(action, class_name,
                                               object_id, key, value) for key,
                                               value in key_value_pairs])
                                self.do_update_list(saved_list)
                                # prevent the original command from executing
                                return ""
                            else:
                                print("Not a valid dictionary")
                        except json.JSONDecodeError as e:
                            print(f"Error decoding JSON: {e}")
                    else:
                        args_list = [arg.strip() for arg in args.split(',')]
                        if action == 'update' and len(args_list) == 2:
                            line = "{} {} {} {}".format(class_name,
                                                        object_id,
                                                        args_list[0],
                                                        args_list[1])
                            self.do_update(line)
                        else:
                            line = "{} {}".format(class_name, object_id)
                            if action == 'destroy':
                                self.do_destroy(line)
                            elif action == 'show':
                                self.do_show(line)
                            elif action == 'update':
                                self.do_update(line)
                            elif action == 'count' and object_id == '':
                                line = class_name
                                self.do_count(line)
                            elif action == 'all' and object_id == '':
                                line = class_name
                                self.do_all(line)
                            elif action == 'create' and object_id == '':
                                line = class_name
                                self.do_create(line)
                            else:
                                print("***Unknown syntax: {}".format(line))
                else:
                    print("***Unknown syntax: {}".format(line))
            else:
                print("***Unknown syntax: {}".format(line))
        else:
            print("***Unknown syntax: {}".format(line))

    def do_count(self, line):
        """Count the instances of a class."""
        words = line.split()

        if not words:
            print("** class name missing **")
        elif words[0] not in storage.classes:
            print("** class doesn't exist **")
        else:
            class_name = words[0]
            instances = [k for k in storage.all() if k.startswith
                         ("{}.".format(class_name))]
            print(len(instances))

    def do_update_list(self, saved_list):
        """Helper function for updating an instance based
        on its ID with a dictionary"""
        for args_str in saved_list:
            args = args_str.replace('[', '')\
                    .replace(']', '').replace('][', ' ').split(' ')
            if len(args) == 5:
                # Extract elements from the sublist
                action, class_name, object_id, key, value = args

                # Create a line from the extracted elements and call do_update
                line = "{} {} {} {}".format(class_name, object_id, key, value)
                self.do_update(line)
            else:
                print("** Invalid no of elements in update argument list **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
