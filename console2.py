#!/usr/bin/python3
"""comment"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage
from datetime import datetime
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


"""It contains the entry poin of the command interpreter for our project"""
class HBNBCommand(cmd.Cmd):
    """It a subclass of the cmd prompt that manage our project"""
    __class = {
        "BaseModel",
        "User",
        "State",
        "City",
        "amenity",
        "Place",
        "Review",
    }
    def __init__(self):
        """It helps to display the '(hbnb)' in the console"""
        cmd.Cmd.__init__(self)
        self.prompt = "(hbnb) "
    def default(self, line):
        """It helps to handle defualt arguments"""
        arg = ""; comad = "";  id = None
        lis = line.split(".")
        """Checks if the Class is valid"""
        if lis[0] in HBNBCommand.__class and len(lis) > 1:
            arg = lis[0]
            lis = lis[1].split('(')
            if len(lis) > 0:
                comad = lis[0]
            lis = line.split('(')
            if (len(lis) > 1 and len(lis[1]) > 3):
                """ Check if the command is 'Update' """
                if (comad == "update"):
                    lis = lis[1]
                    lis = lis[:-1]
                    lis = lis.split(", ")
                    for st in lis:
                        arg += " " + st

                else:
                    lis = lis[1].split(" ")
                    lis = lis[0]
                    id = lis[1:-2]
                    arg +=  " " + id

            """ All the available commands in the console """
            command = {
            "show": "self.do_show(arg)",
             "destroy": "self.do_destroy(arg)",
             "update": "self.do_update(arg)",
             "all": "self.do_all(arg)",
             "count": "self.count(arg)"
            }
            """ It checks if the input from the command line is a command in the console"""
            if comad in command:
                if (comad == "all" and id != None) or (comad == 'count' and id != None):
                    return (super().default(line))
                comad = command[comad]
                eval(comad)
            else:
                return (super().default(line))
        else:
            return (super().default(line))

    def count(self, arg):
        """It Count the number of Specified class in the storage"""
        count = 0
        dic = storage.all()
        objdict = {obj: dic[obj].to_dict() for obj in dic.keys()}
        objdict = objdict.values()
        for di in objdict:
            if di["__class__"] == arg:
                count += 1
        print(count)
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """print a new line when ENTER is press"""
        pass

    def do_create(self, arg):
        """
            Create a new instance of BaseModel, saves it(to the JSON file) and
            prints the id. Ex $create BaseModel
        """
        args = arg.split()
        if (len(arg) == 0):
            print("** class name missing **")
        elif (args[0] not in HBNBCommand.__class):
            print("** class doesn't exist **")
        else:
            class_name = eval(args[0])
            class_name = class_name()
            print(class_name.id)
            class_name.save()
            # print(eval(args[0])().id)
            # storage.save()

    @staticmethod
    def checker(arg):
        """ It helps to check if the input parameters are in their right order"""
        flag = 0
        args = arg.split()
        if (len(args) == 0):
            print("** class name missing **")
            return (1)
        elif (len(args) > 0 and args[0] not in HBNBCommand.__class):
            print("** class doesn't exist **")
            return (1)
        elif (len(args) < 2):
            print("** instance id missing **")
            return (1)
        elif (len(args) > 1):
            concat = args[0] + '.' + args[1].strip('"')
            if (concat not in storage.all()):
                print("** no instance found **")
                return (1)
        return (0)

    def do_show(self, arg):
        """Print the string representation of an instance based on the classs name and id"""
        if (HBNBCommand.checker(arg) != 1):
            args = arg.split()
            concat = args[0] + '.' + args[1]
            objdic = storage.all()
            print(objdic[concat])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if (HBNBCommand.checker(arg) != 1):
            args = arg.split()
            concat = args[0] + '.' + args[1]
            objdic = storage.all()
            del objdic[concat]
            storage.save()

    def do_all(self, arg):
        """Print all string representation of all instaces based or not on the class"""
        objdict = storage.all()
        list_items = []
        if len(arg) == 0:
            for key in objdict.keys():
                list_items.append(str(objdict[key]))
            print(list_items)
        elif (arg not in HBNBCommand.__class):
            print("** class doesn't exist")
        else:
            for value in objdict.values():
                dic = value.to_dict()
                if arg == dic["__class__"]:
                    list_items.append(str(value))
            print(list_items)

    def do_update(self, arg):
        """
            Updates an instance based on the class name and id by adding
            or updating attribute (save the change into the JSON file).
            Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        # check if the given order of input is correct
        if (HBNBCommand.checker(arg) != 1):
            objdict = storage.all()
            args = arg.split()
            class_name = args[0].strip('"') + '.' + args[1].strip('"')
            if (len(args) < 3):
                print("** attribute name missing **")
            elif (len(args) < 4 or len(args) % 2 != 0):
                print("** value missing **")
            else:
                obj = objdict[class_name]
                name = args[2].strip('"')
                strin = args[3]
                #check if it is a dictionary
                if args[2][0] == '{':
                    for i in range(2, len(args)):
                        strin = args[i].strip("{")
                        strin = args[i].strip("}")
                        #check if it a string or integer or float
                        if strin[-1] == ':':
                            name = strin.strip(":")
                            name = name.strip('{')
                            name = name.strip('}')
                            name = name.strip('"')
                            continue
                        cond = {'{', '"', '(', '['}
                        if strin[0] not in cond:
                            try:
                                strin = int(strin)
                            except ValueError:
                                strin = float(strin)
                        else:
                            strin = strin.strip('"')
                            strin = strin.strip('{')

                        # updating the value
                        if (name in obj.to_dict() and type(obj.to_dict()[name]) in {str, int, float}):
                            typ = type(obj.to_dict()[name])
                            obj.__dict__[name] = typ(strin)
                        else:
                            obj.__dict__[name] = strin
                    obj.save()
                else:
                    #check if it a string or integer or float
                    if strin[0] != '"':
                        try:
                            strin = int(strin)
                        except ValueError:
                            strin = float(strin)
                    else:
                        strin = strin.strip('"')
                # updating the value

                    if (name in obj.to_dict() and type(obj.to_dict()[name]) in {str, int, float}):
                        typ = type(obj.to_dict()[name])
                        obj.__dict__[name] = typ(strin)
                    else:
                        obj.__dict__[name] = strin
                obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
