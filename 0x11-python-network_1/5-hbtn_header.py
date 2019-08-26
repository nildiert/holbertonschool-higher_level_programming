#!/usr/bin/python3
"""
Script that takes in a URL and displays the value
of the variable X-Request-Id
"""
import requests
import sys

if __name__ == "__main__":
    try:
        r = requests.head(sys.argv[1])
        print(r.headers['X-Request-Id'])
    except:
        pass
