#!/usr/bin/python3

"""
Clase Rectangle que hereda de la clase Base
y representa un rectángulo.
"""

from models.base import Base


class Rectangle(Base):
    """
    Clase que representa un rectángulo con atributos
    como ancho, alto, posición en X, posición en Y e
    identificador único.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor de la clase Rectangle.

        Parameters:
        - width (int): Ancho del rectángulo.
        - height (int): Alto del rectángulo.
        - x (int): Posición en el eje X.
        - y (int): Posición en el eje Y.
        - id (int): Identificador único del rectángulo.

        Llama al constructor de la clase base (Base)
        y asigna un identificador único. Verifica y
        asigna los parámetros de ancho, alto, posición
        en X e Y.
        """
        super().__init__(id)
        self.check_parameter(width, "width")
        self.check_parameter(height, "height")
        self.check_parameter(x, "x")
        self.check_parameter(y, "y")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, param):
        self.check_parameter(param, "width")
        self.__width = param

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, param):
        self.check_parameter(param, "height")
        self.__height = param

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, param):
        self.check_parameter(param, "x")
        self.__x = param

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, param):
        self.check_parameter(param, "y")
        self.__y = param

    def check_parameter(self, value, param):
        """
        Verifica si un parámetro es un entero y cumple
        con las restricciones especificadas.

        Parameters:
        - value: Valor que se debe verificar.
        - param (str): Nombre del parámetro que se está verificando

        Exceptions:
        - TypeError: Se genera si el valor no es un entero.
        - ValueError: Se genera si el valor no cumple con las restricciones

        Este método se utiliza para garantizar que los
        parámetros pasados al constructor de la clase
        Rectangle sean válidos.

        """
        if type(value) is not int:
            raise TypeError(param + " must be an integer")
        if value <= 0 and param in ("width", "height"):
            raise ValueError(param + " must be > 0")
        if value < 0 and param in ("x", "y"):
            raise ValueError(param + " must be >= 0")

    def area(self):
        """

        Calcula y devuelve el área del rectángulo.

        Return:
        - int: El área del rectángulo

        Esta función calcula el área del rectángulo
        multiplicando su ancho por su alto y devuelve
        el resultado como un número entero.

        """

        return self.__width * self.__height

    def display(self):
        """Muestra una representación visual del rectángulo en la consola"""
        if self.__y > 0:
            print("\n" * self.__y, end="")
        for i in range(self.__height):
            if self.__x > 0:
                print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """

        Devuelve una representación en cadena del rectángulo.

        Return:
        - str: Una cadena que representa el rectángulo

        Esta función genera una representación en cadena del rectángulo

        """

        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """

        Actualiza los atributos del rectángulo utilizando argumentos
        posicionales o palabras clave.

        Parameters:
        - args: Argumentos posicionales que permiten actualizar
                los atributos en un orden específico
                (id, width, height, x, y).
        - kwargs: Palabras clave que permiten actualizar atributos específicos.

        Esta función permite actualizar los atributos del rectángulo,
        utilizando argumentos posicionales o palabras clave.
        Si se proporcionan argumentos posicionales, se actualizan
        en el orden: id, width, height, x, y. Si se proporcionan palabras
        clave, se actualizan los atributos correspondientes si están
        presentes en las palabras clave.

        """
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

    def to_dictionary(self):
        """Return a dict"""
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y,
        }
