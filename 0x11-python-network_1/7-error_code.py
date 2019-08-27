#!/usr/bin/python3
""" This script sends a requests and display the body of the response """

if __name__ == "__main__":

    try:
        import requests
        import sys

        url = sys.argv[1]
        r = requests.get(url)
        if r.status_code > 400:
            print("Error code: {}".format(r.status_code))
        else:
            print(r.text)
    except Exception as err:
        pass
