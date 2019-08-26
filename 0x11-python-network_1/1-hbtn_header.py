#!/usr/bin/python3
# Send a request to the URL

import sys
import urllib.request

try:
    with urllib.request.urlopen(sys.argv[1]) as header:
        print(header.info()['X-Request-Id'])
except Exception as err:
    pass
