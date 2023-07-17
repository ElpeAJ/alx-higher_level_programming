#!/usr/bin/python3


def multiple_returns(sentence):
    length = 0
    char_one = None

    length = len(sentence)
    if (length > 0):
        char_one = sentence[0]

    return (length, char_one)
