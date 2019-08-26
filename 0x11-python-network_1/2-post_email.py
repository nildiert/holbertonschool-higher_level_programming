#!/usr/bin/python3
""" Sends to POST  """

import urllib.request
import urllib.parse
import sys

try:
    data = urllib.parse.urlencode({'email': sys.argv[2]})
    data = data.encode('ascii')
    with urllib.request.urlopen(sys.argv[1], data) as f:
        print(f.read().decode('utf-8'))
except Exception as err:
    pass
