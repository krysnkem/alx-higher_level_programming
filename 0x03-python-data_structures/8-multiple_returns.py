#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence is None:
        return None
    sen_len = len(sentence)
    if sen_len == 0:
        return None
    return (sen_len, sentence[0])
