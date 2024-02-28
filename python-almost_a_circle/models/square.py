#!/usr/bin/python3

"""
Clase Square que hereda de la clase Rectangle
y representa un cuadrado.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor de la clase Square.
        Llama al constructor de la clase base (Rectangle)
        y asigna el tamaño a ancho y alto.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Método para representar el cuadrado como una cadena de texto.
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """
        Propiedad para obtener el tamaño del cuadrado.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Propiedad para establecer el tamaño del cuadrado.
        Actualiza tanto el ancho como el alto.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Método para actualizar los atributos del cuadrado
        a través de argumentos o palabras clave.
        """
        argc = len(args)
        kwargc = len(kwargs)
        modif_attrs = ["id", "size", "x", "y"]

        if argc > 4:
            argc = 4

        if argc > 0:
            for i in range(argc):
                setattr(self, modif_attrs[i], args[i])
        elif kwargc > 0:
            for k, v in kwargs.items():
                if k in modif_attrs:
                    setattr(self, k, v)

    def to_dictionary(self):
        """
        Método para convertir el cuadrado en un diccionario.
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
