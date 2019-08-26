#!/usr/bin/python3
""" This script takes a URL and displays the body of the response """
import sys
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

try:
    req = Request(sys.argv[1])
    response = urlopen(req)
    print(response.read().decode('utf-8'))
except HTTPError as e:
    print('Error code: ', e.code)
