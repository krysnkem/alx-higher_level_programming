#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_emptylist(self):
        self.assertEqual(max_integer([]), None)

    def test_stringvalue(self):
        self.assertRaises(TypeError, max_integer, [1, 'a', -100])

    def test_numeric_string(self):
        self.assertEqual(max_integer('123'), '3')

    def test_list_of_int(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), max_integer([1, 3, 4, 2]))

    def test_integer_input(self):
        self.assertRaises(TypeError, max_integer, 1)

    def test_dict_input(self):
        self.assertRaises(KeyError, max_integer, {"A":1, "B":2})


if __name__== '__man__':
    unittest.main()
