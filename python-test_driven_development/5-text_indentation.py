#!/usr/bin/python3

"""
    Text indentation
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    esp_ch = ""
    for a_char in text:
        if esp_ch == "." or esp_ch == "?" or esp_ch == ":":
            if a_char == " ":
                continue
            else:
                esp_ch = ""
                print(a_char, end="")
                continue
        if a_char == "." or a_char == "?" or a_char == ":":
            print(a_char)
            print("")
            esp_ch = a_char
        else:
            print(a_char, end="")
