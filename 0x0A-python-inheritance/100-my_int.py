#!/usr/bin/python3
"""Define the MyInt class"""


class MyInt(int):
    """the MyInt class that extends the int class"""

    def __init__(self, num):
        self.num = num

    def __eq__(self, other):
        if self.num == other:
            return False
        else:
            return True

    def __ne__(self, other):
        if self.num != other:
            return False
        else:
            return True
