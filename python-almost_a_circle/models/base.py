#!/usr/bin/python3

"""
Clase Base que se utiliza para gestionar
objetos con un identificador único.
"""

import json
from os import path


class Base:
    """
    Atributo de clase para realizar
    un seguimiento del número de
    objetos creados.
    """

    __nb_objects = 0

    """
    Constructor de la clase Base.
    Si no se proporciona un "id",
    incrementa el contador y asigna
    un valor único. Si se proporciona
    un "id", lo asigna al objeto.
    """

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictonaries):
        """
        Convierte una lista de diccionarios
        en una cadena JSON. Si la lista es
        nula o vacía, devuelve una cadena vacía.
        """
        if list_dictonaries is None or len(list_dictonaries) == 0:
            return "[]"
        return json.dumps(list_dictonaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Guarda una lista de objetos en
        un archivo JSON. El nombre del
        archivo se deriva del nombre de la clase.
        """
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as f:
            if list_objs is None:
                return f.write(cls.to_json_string(None))

            json_attributes = []

            for elem in list_objs:
                json_attributes.append(elem.to_dictionary())
            return f.write(cls.to_json_string(json_attributes))

    @staticmethod
    def from_json_string(json_string):
        """
        Convierte una cadena JSON en una
        lista de diccionarios.Si la cadena
        es nula o vacía, devuelve una lista vacía.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Crea un objeto de la clase a partir de un diccionario.
        Si la clase se llama "Square", crea un cuadrado predeterminado.
        Si es "Rectangle", crea un rectángulo predeterminado.
        Luego, actualiza sus atributos con el diccionario.
        """
        if cls.__name__ == "Square":
            concept = cls(3)

        if cls.__name__ == "Rectangle":
            concept = cls(3, 3)

        concept.update(**dictionary)
        return concept

    @classmethod
    def load_from_file(cls):
        """
        Carga objetos desde un archivo JSON y
        los convierte en instancias de la clase.
        """
        filename = cls.__name__ + ".json"

        if not path.exists(filename):
            return []

        with open(filename, mode="r", encoding="utf-8") as f:
            objs = cls.from_json_string(f.read())
            ins = []

            for element in objs:
                ins.append(cls.create(**element))

            return ins
