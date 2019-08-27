#!/usr/bin/python3
""" GitHub credentials """

if __name__ == "__main__":

    import requests
    import sys

    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]

    r = requests.get(url, auth=(username, password))
    print(r.json().get('id'))
