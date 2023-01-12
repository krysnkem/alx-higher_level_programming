#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    ta_len, tb_len = len(tuple_a), len(tuple_b)
    if ta_len < 2:
        tuple_a += (0,) * (2 - ta_len)

    if tb_len < 2:
        tuple_b += (0,) * (2 - tb_len)

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
