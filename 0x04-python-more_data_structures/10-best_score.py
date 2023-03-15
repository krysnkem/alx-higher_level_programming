#!/usr/bin/python3
def best_score(a_dictionary):

    """.returns a key with the biggest value."""
    if not a_dictionary:
        return None

    max_key = None
    max_num = 0
    for k, v in a_dictionary.items():
        if v > max_num:
            max_num = v
            max_key = k
    return max_key
