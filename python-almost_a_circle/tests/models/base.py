#!/usr/bin/python

"""
Clase Base que se utiliza para gestionar objetos con un identificador único.
"""


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
