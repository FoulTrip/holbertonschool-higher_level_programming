#!/usr/bin/python3

"""
Clase Rectangle que hereda de la clase Base y representa un rectángulo.
"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        # Llama al constructor de la clase base (Base) y asigna un identificador único.
        super().__init__(id)

        # Verifica y asigna los parámetros de ancho (width), alto (height), posición en X (x), y posición en Y (y).
        self.check_parameter(width, "width")
        self.check_parameter(height, "height")
        self.check_parameter(x, "x")
        self.check_parameter(y, "y")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    # Propiedad para obtener el ancho del rectángulo.
    @property
    def width(self):
        return self.__width

    # Propiedad para establecer el ancho del rectángulo.
    @width.setter
    def width(self, param):
        self.check_parameter(param, "width")
        self.__width = param

    # Propiedad para obtener la altura del rectángulo.
    @property
    def height(self):
        return self.__height

    # Propiedad para establecer la altura del rectángulo.
    @height.setter
    def height(self, param):
        self.check_parameter(param, "height")
        self.__height = param

    # Propiedad para obtener la posición en X del rectángulo.
    @property
    def x(self):
        return self.__x

    # Propiedad para establecer la posición en X del rectángulo.
    @x.setter
    def x(self, param):
        self.check_parameter(param, "x")
        self.__x = param

    # Propiedad para obtener la posición en Y del rectángulo.
    @property
    def y(self):
        return self.__y

    # Propiedad para establecer la posición en Y del rectángulo.
    @y.setter
    def y(self, param):
        self.check_parameter(param, "y")
        self.__y = param

    # Método para verificar si un parámetro es un entero y cumple con las restricciones.
    def check_parameter(self, value, param):
        if type(value) is not int:
            raise TypeError(param + " must be an integer")

        if value <= 0 and param in ("width", "height"):
            raise ValueError(param + " must be > 0")

        if value < 0 and param in ("x", "y"):
            raise ValueError(param + " must be >= 0")

    # Método para calcular el área del rectángulo.
    def area(self):
        return self.__width * self.__height

    # Método para mostrar el rectángulo en la consola.
    def display(self):
        if self.__y > 0:
            print("\n" * self.__y, end="")

        for i in range(self.__height):
            if self.__x > 0:
                print(" " * self.__x, end="")

            print("#" * self.__width)

    # Método para representar el rectángulo como una cadena de texto.
    def __str__(self):
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    # Método para actualizar los atributos del rectángulo a través de argumentos o palabras clave.
    def update(self, *args, **kwargs):
        argc = len(args)
        kwargc = len(kwargs)
        modif_attrs = ["id", "width", "height", "x", "y"]

        if argc > 5:
            argc = 5

        if argc > 0:
            for i in range(argc):
                setattr(self, modif_attrs[i], args[i])
        elif kwargc > 0:
            for k, v in kwargs.items():
                if k in modif_attrs:
                    setattr(self, k, v)

    # Método para convertir el rectángulo en un diccionario.
    def to_dictionary(self):
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y,
        }
