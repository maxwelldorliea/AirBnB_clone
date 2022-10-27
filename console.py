#!/bin/python3

"""
This is The Console Module.
"""
import cmd, json
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt: str = "(hbnb)"
    file = None

    def is_valid_model(self, model):
        try:
            with open('file.json', 'r', encoding='utf-8') as f:
                objs = json.loads(f.read())
            for obj in objs.values():
                if model in obj.values():
                    return True
            return False
        except Exception:
            pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    def do_EOF(self, line):
        "EOF or ctrl^D command to exit the program"
        return True
    def do_create(self, line):
        if not line:
            print('** class name missing **')
        elif not self.is_valid_model(line):
            print("** class doesn't exist **")
        else:
            base = BaseModel()
            base.save()
            print(base.id)
    def do_show(self, line):
        arg = line.split()
        if not line:
            print('** class name missing **')
        elif not self.is_valid_model(arg[0]):
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
        arg = line.split()
        if not line:
            print('** class name missing **')
        elif not self.is_valid_model(arg[0]):
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
                if not objs_arr:
                    print("** class doesn't exist **")
                else:
                    print(objs_arr)
            except Exception:
                pass

    def do_update(self, line):
        arg = line.split()
        with open('file.json', 'r', encoding='utf-8') as f:
            objs = json.loads(f.read())
        if not line:
            print('** class name missing **')
        elif not self.is_valid_model(arg[0]):
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        elif not arg[0] + '.' + arg[1] in objs:
            print("** no instance found **")
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
                objs = json.dump(objs, f)



if __name__ == '__main__':
    HBNBCommand().cmdloop()
