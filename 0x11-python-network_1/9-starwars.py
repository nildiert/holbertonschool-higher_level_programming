#!/usr/bin/python3
""" Sends a search request to the Star Wars API """

if __name__ == "__main__":

    import requests
    import sys

    url = "https://swapi.co/api/people"
    try:
        q = {"search": sys.argv[1]}
    except:
        q = {"search": ""}
    r = requests.post(url, params=q)
    print("Number of results: {}".format(r.json().get('count')))
    result = r.json().get('results')
    for item in result:
        print(item['name'])
