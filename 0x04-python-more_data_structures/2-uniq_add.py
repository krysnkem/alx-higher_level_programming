#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    uniq_list = set(my_list)
    for x in uniq_list:
        result += x

    return result
