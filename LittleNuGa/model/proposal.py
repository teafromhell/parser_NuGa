import json

__author__ = 'tea'


class Proposal:
    descr = None
    price = None
    stuff = None
    ref = None
    name = None
    def __init__(self, name, descr, price, stuff, ref):
        self.descr = descr
        self.price = price
        self.stuff = stuff
        self.ref = ref
        self.name = name

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

