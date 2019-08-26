#!/usr/bin/python3
""" This script takes a URL and displays the body of the response """
import sys
import urllib.request
from urllib.error import HTTPError

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            html = response.read()
            print("{}".format(html.decode('utf-8')))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
    except:
        pass
