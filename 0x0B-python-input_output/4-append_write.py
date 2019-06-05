#!/usr/bin/python3


def append_write(filename="", text=""):
    size = 0
    with open(filename, encoding="utf-8", mode='a') as myFile:
        return myFile.write(text)
