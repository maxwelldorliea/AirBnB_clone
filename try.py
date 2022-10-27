#!/bin/python3
from datetime import datetime as dtime
from uuid import uuid4
class A:
    def __init__(self) -> None:
        self.id = str(uuid4())
        self.created_at = dtime.now()
        self.updated_at = dtime.now()

    def __str__(self) -> str:
        return "max"

    def to_dict(self):
        out = self.__dict__
        out['created_at'] = out['created_at'].isoformat()
        out['updated_at'] = out['updated_at'].isoformat()
        return out

class B:
    def createA(self):
        a = eval('A')
        c = a()
        print(c.to_dict())
        print(self.__new__(a))

b = B()

b.createA()
