#!/usr/bin/python3

"""
    Text indentation
"""

def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: '.', '?' and ':' """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""
    special_chars = {".", "?", ":"}

    for char in text:
        new_text += char

        if char in special_chars:
            new_text += "\n"

    print("\n".join(line.strip() for line in new_text.split("\n")))
