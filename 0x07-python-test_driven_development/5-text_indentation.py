#!/usr/bin/python3
"""
The ``5-text_indentation`` module
defines a function that prints a text with 2 new lines after
each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    print sentences out of a string
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    beginning = True
    text = text.strip()
    for c in text:
        if beginning and c == ' ':
            continue
        print(c, end="")
        beginning = False
        if c in ['.', '?', ':']:
            print("\n")
            beginning = True
