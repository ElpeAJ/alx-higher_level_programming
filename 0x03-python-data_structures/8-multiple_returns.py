#!/usr/bin/python3

def multiple_returns(sentence):
    sentence_tuple = ()
    length_of_string = len(sentence)
    if length_of_string == 0:
        sentence_tuple = (length_of_string, None)
    else:
        sentence_tuple = (length_of_string, sentence[0])
    return sentence_tuple

