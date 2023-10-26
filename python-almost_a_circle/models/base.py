#!/usr/bin/python3

"""
Clase Base que se utiliza para gestionar objetos con un identificador único.
"""

import json
from os import path


class Base:
    """
    Atributo de clase para realizar un seguimiento del número de objetos creados.
    """

    __nb_objects = 0

    """
    Constructor de la clase Base. Si no se proporciona un "id", incrementa el contador
    y asigna un valor único. Si se proporciona un "id", lo asigna al objeto.
    """

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id


@staticmethod
def to_json_string(list_dictonaries):
    if list_dictonaries is None or len(list_dictonaries) == 0:
        return "[]"
    return json.dumps(list_dictonaries)


@classmethod
def save_to_file(cls, list_objs):
    filename = cls.__name__ + "json"
    with open(filename, mode="w", encoding="utf-8") as f:
        if list_objs == None:
            return f.write(cls.to_json_string(None))

        json_attributes = []

        for elem in list_objs:
            json_attributes.append(elem.to_dictionary())
        return f.write(cls.to_json_string(json_attributes))


@staticmethod
def from_json_string(json_string):
    if json_string == None or len(json_string) == 0:
        return []
    return json.loads(json_string)


@classmethod
def create(cls, **dictionary):
    if cls.__name__ == "square":
        concept = cls(3)

    if cls.__name__ == "Rectangle":
        concept = cls(3, 3)

    concept.update(**dictionary)
    return concept

@classmethod
def load_from_file(cls):
    filename = cls.__name__ + ".json"

    if path.exists(filename) is False:
        return []

    with open(filename, mode="r", encoding="utf-8") as f:
        objs = cls.from_json_string(f.read())
        ins = []

        for element in objs:
            ins.append(cls.create(**element))

        return ins
