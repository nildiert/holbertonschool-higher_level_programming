#!/usr/bin/python3
""" post request in api """

if __name__ == "__main__":
    try:
        import requests
        import sys

        url = "http://0.0.0.0:5000/search_user"
        try:
            q = {'q': sys.argv[1]}
        except:
            q = {'q': ""}
        try:
            r = requests.post(url, q)
            if len(r.json()) == 0:
                print("No result")
            else:
                print("[{}] {}".format(
                    r.json().get('id'), r.json().get('name'))
                )
        except:
            print("Not a valid JSON")

    except Exception as err:
        pass
