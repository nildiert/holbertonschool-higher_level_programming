#!/usr/bin/python3


def write_file(filename="", text=""):
    with open(filename, encoding="utf-8", mode='w') as myFile:
        return myFile.write(text)
