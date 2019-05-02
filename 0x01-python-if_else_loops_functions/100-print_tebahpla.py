#!/usr/bin/python3
for c in range(123, 96, -1):
    if (c != 123):
        print ("{}".format(chr(c)) if c % 2 == 0 else chr(c - 32), end="")
