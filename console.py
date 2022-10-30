#!/usr/bin/python3
"""This is The Console Module."""
import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """This model represent our console."""

    prompt: str = "(hbnb)"
    file = None
    class_name = ['BaseModel', 'State', 'User']
    class_name += ['City', 'Amenity', 'Place', 'Review']

    def parse_input(self, cmd):
        """Parse string pass to it."""
        arg = cmd.replace('(', ' ').replace('"', '').replace("'", "")
        arg = arg.replace('.', ' ').replace(')', '')
        return arg

    def emptyline(self) -> None:
        """Do nothing when empty line and enter is receive."""
        return

    def default(self, line: str) -> None:
        """Find the right cmd and execute it."""
        cmd = {
                'all': self.do_all,
                'count': self.count,
                'show': self.do_show,
                'destroy': self.do_destroy,
                'update': self.do_update
            }
        arg = self.parse_input(line).split()

        if len(arg) < 2:
            return super().default(line)

        if arg[1] in cmd:
            func = cmd[arg[1]]
            func(line)
        else:
            return super().default(line)

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """EOF or ctrl^D command to exit the program."""
        return True

    def do_create(self, line):
        """Create an available model and save it in our file storage."""
        if not line:
            print('** class name missing **')
        elif line not in self.class_name:
            print("** class doesn't exist **")
        else:
            base = eval(f'{line}()')
            base.save()
            print(base.id)

    def do_show(self, line):
        """Retrieve an instance of a supported model from our file storage."""
        arg = self.parse_input(line).replace('show', '').split()
        if not line:
            print('** class name missing **')
        elif not arg[0] in self.class_name:
            print("** class doesn't exist **")
        elif len(arg) != 2:
            print("** instance id missing **")
        else:
            id_ = arg[0] + '.' + arg[1]
            try:
                with open('file.json', 'r', encoding='utf-8') as f:
                    objs = json.loads(f.read())
                if id_ in objs:
                    out = objs[id_]
                    name = out['__class__']
                    base = eval(f"{name}(**out)")
                    print(base)
                else:
                    print("** no instance found **")
            except Exception:
                print("** no instance found **")

    def do_destroy(self, line):
        """Delete an instance of a supported model from our file storage."""
        arg = self.parse_input(line).replace('destroy', '').split()
        if not line:
            print('** class name missing **')
        elif not arg[0] in self.class_name:
            print("** class doesn't exist **")
        elif len(arg) != 2:
            print("** instance id missing **")
        else:
            id_ = arg[0] + '.' + arg[1]
            try:
                with open('file.json', 'r', encoding='utf-8') as f:
                    objs = json.loads(f.read())
                if id_ in objs:
                    del objs[id_]
                    with open('file.json', 'w', encoding='utf-8') as f:
                        json.dump(objs, f, indent=4)
                else:
                    print("** no instance found **")
            except Exception:
                print("** no instance found **")

    def do_all(self, line):
        """Retrieve every model instances from our file storage."""
        line = self.parse_input(line).replace('all', '').replace(' ', '')
        objs = {}
        objs_arr = []
        try:
            with open('file.json', 'r', encoding='utf-8') as f:
                objs = json.loads(f.read())
        except Exception:
            pass
        if not line:
            for obj in objs.values():
                name = obj['__class__']
                inst = eval(f'{name}(**obj)')
                objs_arr.append(str(inst))
            print(objs_arr)
        elif line not in self.class_name:
            print("** class doesn't exist **")
        else:
            for obj in objs.values():
                name = obj['__class__']
                if name == line:
                    inst = eval(f'{name}(**obj)')
                    objs_arr.append(str(inst))
            print(objs_arr)

    def do_update(self, line):
        """Update an instance of a supported model from our file storage."""
        arg = self.parse_input(line).replace('update', '').split(maxsplit=3)
        cnvt = {
                "int" : int,
                "float" : float,
                "str" : str,
                "dict" : self.to_dict,
                "list" : self.to_list
            }
        try:
            with open('file.json', 'r', encoding='utf-8') as f:
                objs = json.loads(f.read())
            if not line:
                print('** class name missing **')
            elif arg[0] not in self.class_name:
                print("** class doesn't exist **")
            elif len(arg) < 2:
                print("** instance id missing **")
            elif arg[0] + '.' + self.parse_input(arg[1]) not in objs:
                print("** no instance found **")
            elif len(arg) < 3:
                print("** attribute name missing **")
            elif len(arg) < 4:
                print("** value missing **")
            else:
                inst = eval(f'{arg[0]}()')
                k, val = arg[2], arg[3].replace('"', '').replace("'", "")
                key = arg[0] + '.' + self.parse_input(arg[1])
                typ = type(getattr(inst, k, None))
                if typ:
                    if typ.__name__ in cnvt:
                        func = cnvt[typ.__name__]
                        val = func(val)
                obj = objs[key]
                obj[k] = val
                with open('file.json', 'w', encoding='utf-8') as f:
                    json.dump(objs, f, indent=4)
        except Exception:
            pass

    def count(self, line):
        """
        Count the total instances of.

        a supported model from our file storage.
        """
        cnt = 0
        line = self.parse_input(line).replace('count', '').replace(' ', '')
        if line not in self.class_name:
            print("** class doesn't exist **")
            return
        try:
            with open('file.json', 'r', encoding='utf-8') as f:
                objs = json.loads(f.read())
            for obj in objs.values():
                name = obj['__class__']
                if name == line:
                    cnt += 1
            print(cnt)
        except Exception:
            pass

    def to_dict(self, obj):
        """Convert @obj to dict."""
        return eval(obj)

    def to_list(self, lst):
        """Convert @lst to list."""
        lst = [str(v) for v in eval(lst)]
        print(lst)
        return lst

if __name__ == '__main__':
    HBNBCommand().cmdloop()
