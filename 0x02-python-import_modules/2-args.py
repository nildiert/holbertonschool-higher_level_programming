#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    for i in range(1, len(sys.argv)):
        print("{:d}: {}".format(i, sys.argv[i]))
