#!/bin/python3

"""
This is The Console Module.
"""
import cmd, json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    prompt: str = "(hbnb)"
    file = None
    class_name = ['BaseModel', 'State', 'User', 'City', 'Amenity', 'Place', 'Review']

    def default(self, line: str) -> None:
        cmd = {
                'all' : self.do_all,
                'count' : self.count,
                'show' : self.do_show,
                'destroy' : self.do_destroy,
                'update' : self.do_update
            }
        arg = line.replace('(', ' ').replace('"', '').replace("'", "").replace('.', ' ').replace(')', '').replace(",", "").split()

        if arg[1] in cmd:
            func = cmd[arg[1]]
            arg[0], arg[1] = arg[1], arg[0]
            func(" ".join(arg[1:]))
        else:
            return super().default(line)

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    def do_EOF(self, line):
        "EOF or ctrl^D command to exit the program"
        return True
    def do_create(self, line):
        if not line:
            print('** class name missing **')
        elif not line in self.class_name:
            print("** class doesn't exist **")
        else:
            base = eval(f'{line}()')
            base.save()
            print(base.id)
    def do_show(self, line):
        arg = line.replace('"', '').replace("'", "").split()
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
        arg = line.replace('(', ' ').replace('.', ' ').replace(')', '').split()
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
        if not line:
            objs_arr = []
            try:
                with open('file.json', 'r', encoding='utf-8') as f:
                    objs = json.loads(f.read())
                for obj in objs.values():
                    name = obj['__class__']
                    inst = eval(f'{name}(**obj)')
                    objs_arr.append(str(inst))
                print(objs_arr)
            except Exception:
                pass
        elif not line in self.class_name:
            print("** class doesn't exist **")
        else:
            objs_arr = []
            try:
                with open('file.json', 'r', encoding='utf-8') as f:
                    objs = json.loads(f.read())
                for obj in objs.values():
                    name = obj['__class__']
                    if name == line:
                        inst = eval(f'{name}(**obj)')
                        objs_arr.append(str(inst))
                    print(objs_arr)
            except Exception:
                pass

    def do_update(self, line):
        arg = line.split()
        try:
            with open('file.json', 'r', encoding='utf-8') as f:
                objs = json.loads(f.read())
            if not line:
                print('** class name missing **')
            elif not arg[0] in self.class_name:
                print("** class doesn't exist **")
            elif len(arg) < 2:
                print("** instance id missing **")
            elif not arg[0] + '.' + arg[1] in objs:
                print("** no instance found **")
            elif len(arg) == 3:
                try:
                    new_obj = json.loads(arg[-1])
                    key = arg[0] + '.' + arg[1]
                    obj = objs[key]
                    for k, v in new_obj.items():
                        obj[k] = v
                    with open('file.json', 'w', encoding='utf-8') as f:
                        json.dump(objs, f)
                    return
                except Exception as err:
                    print(err)
            elif len(arg) < 3:
                print("** attribute name missing **")
            elif len(arg) < 4:
                print("** value missing **")
            else:
                k, val = arg[2], arg[3].replace('"', '').replace("'", "")
                key = arg[0] + '.' + arg[1]
                obj = objs[key]
                obj[k] = val
                with open('file.json', 'w', encoding='utf-8') as f:
                    json.dump(objs, f)
        except Exception:
            pass

    def count(self, line):
        cnt = 0
        if not line in self.class_name:
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
