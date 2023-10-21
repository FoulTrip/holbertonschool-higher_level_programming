#!/usr/bin/python3


def class_to_json(obj):
    dicc_obj = dict()

    for key in obj.__dict__:
        value = getattr(obj, key)

        if isinstance(value, (str, int, bool)):
            dicc_obj[key] = value
        elif isinstance(value, list):
            dicc_obj[key] = list(value)
        elif isinstance(value, dict):
            dicc_obj[key] = dict(value)
        else:
            raise TypeError(f"Tipo no serializable: {type(value).__name__}")

    return dicc_obj
