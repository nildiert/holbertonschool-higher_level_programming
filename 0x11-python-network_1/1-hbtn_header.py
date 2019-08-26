#!/usr/bin/python3
# Send a request to the URL

from sys import argv
from urllib.request import Request, urlopen

try:
    response = urlopen(argv[1])
    print(response.info()['X-Request-Id'])
except:
    pass
