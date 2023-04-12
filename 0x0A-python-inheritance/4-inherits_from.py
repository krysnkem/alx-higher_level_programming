#!/usr/bin/python3
"""4-inherits_from defines a method for checking if an object
 is aa subclass of a class
 """


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class
    that inherited (directly or indirectly)
    from the specified class ; otherwise False
    """

    return issubclass(obj.__class__, a_class) and type(obj) != a_class
