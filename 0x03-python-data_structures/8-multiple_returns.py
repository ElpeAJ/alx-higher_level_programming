#!/usr/bin/python3

def multiple_returns(sentence):
    print("length of string is: " + str(len(sentence)) + " - First character: " + tuple(sentence)[0])
    if len(tuple(sentence)) == 0:
        return (None)

