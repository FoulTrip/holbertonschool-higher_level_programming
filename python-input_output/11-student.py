#!/usr/bin/python3

"""Student to disk and reload """


class Student:
    """defines a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        that retrieves a dictionary
        representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}

    def reload_from_json(self, json):
        """that replaces all attributes of the Student instance"""
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
