#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if (i % 3 != 0 and i % 5 != 0):
            print("{:d}".format(i), end=' ')
        else:
            print("{}".format("Fizz" if ((i % 3) == 0) else ""), end='')
            print("{}".format("Buzz" if ((i % 5) == 0) else ""), end=' ')
