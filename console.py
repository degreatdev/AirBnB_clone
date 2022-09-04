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
if __name__ == "__main__":
    HBNBCommand().cmdloop()
