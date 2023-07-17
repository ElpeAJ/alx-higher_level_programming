#!/usr/bin/python3

def multiple_returns(sentence):
    sentence_tuple = ()
    length_of_string = len(sentence)
    if length_of_string < 1:
        sentence_tuple = (0, None)
    else:
        sentence_tuple = (length_of_string, sentence[0])
    return sentence_tuple

