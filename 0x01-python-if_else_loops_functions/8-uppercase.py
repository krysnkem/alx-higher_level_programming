#!/usr/bin/python3
def islower(c):
    return ord(c) in range(97, 123)


def toUpper(c):
    return chr(ord(c) - 32)


def uppercase(str):
    str_cpy = ""
    for c in str:
        str_cpy = str_cpy + "{}".format(toUpper(c) if islower(c) else c)
    print(str_cpy)
