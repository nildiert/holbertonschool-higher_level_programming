#!/usr/bin/python3
def uppercase(str):
    for c in str:
            print("{}".format(chr(ord(c) - 32)
                              if (ord(c) > 96 and ord(c) < 123)
                              else c), end='')
    print("")
