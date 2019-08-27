#!/usr/bin/python3
""" send email  in post  """

if __name__ == "__main__":

    import requests
    import sys

    try:
        url = sys.argv[1]
        email = {'email': sys.argv[2]}
        r = requests.post(url, data=email)
        print(r.text)
    except Exception as err:
        pass
