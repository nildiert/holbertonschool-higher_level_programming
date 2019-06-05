#!/usr/bin/python3


def number_of_lines(filename=""):
    size = 0
    with open(filename, encoding="utf-8") as myFile:
        for line in myFile:
            size += 1
        return size
