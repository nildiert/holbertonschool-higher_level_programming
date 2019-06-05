#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    size = 0
    with open(filename, encoding="utf-8") as myFile:
        if nb_lines <= 0:
            print("{}".format(myFile.read()))
        while size < nb_lines:
            line = myFile.readline()
            print(line, end="")
            size += 1
