#!/usr/bin/python3

"""Load, add, save """
import json
import os
import sys


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file,
    using a JSON representation
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    """creates an Object from a “JSON file”"""
    with open(filename) as f:
        return json.load(f)


def add_items(arguments):
    # Compruebo si el archivo 'add_item.json' ya existe
    if os.path.exists("add_item.json"):
        my_list = load_from_json_file("add_item.json")
    else:
        my_list = []

    # Añado argumentos de línea de comandos a la lista
    my_list.extend(arguments)

    # Guardo la lista actualizada en 'add_item.json'
    save_to_json_file(my_list, "add_item.json")


if __name__ == "__main__":
    # Get command-line arguments excluding the script name
    arguments = sys.argv[1:]
    add_items(arguments)
