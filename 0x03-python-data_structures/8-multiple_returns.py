#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = 0
    if sentence is not None:
        lenght = len(sentence)
    return (lenght, None if sentence is None else sentence[0])
