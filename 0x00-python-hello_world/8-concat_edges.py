#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
       language that combines remarkable power with very clear syntax"
str = f"{str[:-17]}"
str = f"{str[39:66]} {str[113:117]} {str[:6]}"
print(str)
