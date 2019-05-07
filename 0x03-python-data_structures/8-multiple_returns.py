#!/usr/bin/python3
def multiple_returns(sentence):
        lenght = len(sentence)
        return (lenght, sentence[0] if lenght > 0 else None)
