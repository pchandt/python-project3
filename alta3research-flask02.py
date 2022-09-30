#!/usr/bin/env python3
""" A script that demonstrate proficiency with the requests HTTP library"""
import json

import requests
from pprint import pprint  # python3 -m pip install pprint
import pandas as pd  # python3 -m pip install pandas

# URL for endpoint that returns json data for the list sde_apprenticeship
URL = "http://127.0.0.1:2224/json"


def main():
    # Send HTTPS GET to the Flask API that returns json endpoint
    resp = requests.get(URL)
    # strip off JSON response and convert to PYTHONIC LIST / DICT
    respjson = resp.json()
    for i in respjson:
        pprint(i.keys())
        if "instructor" in i.keys():
            pprint(f"Instructor info: {i['instructor']}")

    # Normalizes json data into a flat table using pandas
    norm = pd.json_normalize(respjson)
    # pretty-print the normalized json data
    pprint(norm)

    # new dictionary to append to sde_apprenticeship list
    new_data = {'course': 'AWS',
                'duration': 'one week',
                'projects': 0,
                'labs': 0,
                'instructor': {'name': 'Richard',
                               'email': 'richard@example.com'}
                }

    # json.dumps takes a python object and returns it as a JSON string
    new_data= json.dumps(new_data)
    # requests.post requires URL to send request and json string to attach a request
    result = requests.post(URL, json=new_data)
    # pretty-print the response back from our POST request
    pprint(result.json())


# invoke the main function
if __name__ == "__main__":
    main()
