#!/usr/bin/python3
"""Define the hbnb console."""

import cmd
import sys
import re
import json
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Console class."""

    prompt = ' (hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def emptyline(self):
        """EmptyLine."""
        pass

    def do_EOF(self, arg):
        """End of file."""
        return True

    def do_create(self, line):
        """Create: Creates new instance of BaseModel."""
        slash = line.split()
        classes = ["User", "State", "City", "Place",
                   "Amenity", "Review", "BaseModel"]

        if not slash:
            print("** class name missing **")
        else:
            if slash[0] in classes:
                new_model = eval(slash[0] + "()")
                new_model.save()
                print(new_model.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        """Gives string representation of an instance."""
        found = 0
        dics = (storage.all())
        slash = line.split()
        classes = ["User", "State", "City", "Place",
                   "Amenity", "Review", "BaseModel"]

        if not slash:
            print("** class name missing **")
        else:
            if slash[0] in classes:
                found = 1

            if found == 0:
                print("** class doesn't exist **")
            else:
                if len(slash) == 1:
                    print("** instance id missing **")
                elif len(slash) > 1:
                    found = 0
                    for key in dics:
                        for sub_key in dics[key]:
                            if sub_key == "id":
                                if dics[key][sub_key] == slash[1]:
                                    found = 1
                    if found == 0:
                        print("** no instance found **")
                    else:
                        key = slash[0] + "." + slash[1]
                        if key in dics:
                            dic_model = (dics[key])
                            model = eval(slash[0]+"(**dic_model)")
                            print(model)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id."""
        found = 0
        dics = (storage.all())
        slash = line.split()
        classes = ["User", "State", "City", "Place",
                   "Amenity", "Review", "BaseModel"]

        if not slash:
            print("** class name missing **")
        else:
            if slash[0] in classes:
                found = 1

            if found == 0:
                print("** class doesn't exist **")
            else:
                if len(slash) == 1:
                    print("** instance id missing **")
                elif len(slash) > 1:
                    found = 0
                    for key in dics:
                        for sub_key in dics[key]:
                            if sub_key == "id":
                                if dics[key][sub_key] == slash[1]:
                                    found = 1
                    if found == 0:
                        print("** no instance found **")
                    else:
                        key = slash[0] + "." + slash[1]
                        if key in dics:
                            dics.pop(key, None)
                            with open(FileStorage._FileStorage__file_path,
                                      mode="w", encoding='utf-8') as file:
                                json.dump(dics, file)

    def do_all(self, line):
        """Prints all string representation of all instances."""
        found = 0
        dics = (storage.all())
        slash = line.split()
        new_list = []
        classes = ["User", "State", "City", "Place",
                   "Amenity", "Review", "BaseModel"]

        if len(slash) > 0:
            if slash[0] in classes:
                found = 1

        if len(slash) == 0:
            for key in dics:
                dic_model = (dics[key])
                model = eval(key.split(".")[0]+"(**dic_model)")
                new_list.append(model.__str__())
            print(new_list)

        elif found == 1:
            for key in dics:
                dic_model = (dics[key])
                if key.split(".")[0] == slash[0]:
                    model = eval(slash[0]+"(**dic_model)")
                    new_list.append(model.__str__())
            print(new_list)

        elif found == 0 and len(slash) > 0:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id\n"""
        found = 0
        dics = (storage.all())
        slash = line.split()
        classes = ["User", "State", "City", "Place",
                   "Amenity", "Review", "BaseModel"]
        dic_classes = {"User": User, "State": State,
                       "City": City, "Place": Place,
                       "Amenity": Amenity, "Review": Review,
                       "BaseModel": BaseModel}

        if not slash:
            print("** class name missing **")
        else:
            if slash[0] in classes:
                found = 1

            if found == 0:
                print("** class doesn't exist **")
            else:
                if len(slash) == 1:
                    print("** instance id missing **")
                elif len(slash) > 1:
                    found = 0
                    for key in dics:
                        for sub_key in dics[key]:
                            if sub_key == "id":
                                if dics[key][sub_key] == slash[1]:
                                    found = 1
                    if found == 0:
                        print("** no instance found **")
                    else:
                        if len(slash) == 2:
                            print("** attribute name missing **")
                        elif len(slash) == 3:
                            print("** value missing **")
                        else:
                            key = slash[0] + "." + slash[1]
                            dic_model = dics[key]
                            dics.pop(key, None)
                            modelo = eval(slash[0]+"(**dic_model)")
                            value = slash[3]
                            if value[0] == "\"" and value[-1] == "\"":
                                value = value[1:-1]
                            if getattr(modelo, slash[2], "nohay") != "nohay":
                                if type(getattr(modelo, slash[2])) == int:
                                    value = int(value)
                                elif type(getattr(modelo, slash[2])) == float:
                                    value = float(value)
                            setattr(dic_classes[slash[0]], slash[2], value)
                            modelo.save()

    def do_count(self, line):
        """count number of instances\n"""
        found = 0
        cont = 0
        dics = (storage.all())
        slash = line.split()
        classes = ["User", "State", "City", "Place",
                   "Amenity", "Review", "BaseModel"]

        if not slash:
            print("** class name missing **")
        else:
            if slash[0] in classes:
                found = 1

            if found == 0:
                print("** class doesn't exist **")
            else:
                for key in dics:
                    for sub_key in dics[key]:
                        if dics[key][sub_key] == slash[0]:
                            cont += 1
                print(cont)

    def default(self, line):
        """Method to use the "User.method" way\n"""
        cmds = {"create": self.do_create, "show": self.do_show,
                "all": self.do_all, "destroy": self.do_destroy,
                "update": self.do_update, "count": self.do_count}
        slash = line.split(".", 1)
        modelo = slash[0]
        semi_cmd = slash[1].split("(", 1)
        cmd = semi_cmd[0]
        args = semi_cmd[1].split(", ")

        if cmd in cmds:
            if len(args) >= 3:
                linea = modelo + " " + args[0][1:-1]\
                    + " " + args[1][1:-1] + " " + args[2][0:-1]
            elif len(args) == 2:
                linea = modelo + " " + args[0][1:-1] + " " + args[1][1:-1]
            elif len(args) == 1:
                linea = modelo + " " + args[0][1:-2]
            cmds[cmd](linea)
        else:
            print("*** Unknown syntax:", line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
