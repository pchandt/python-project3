#!/usr/bin/env python3
""" A script that demonstrate proficiency with the requests HTTP library"""

import requests
from pprint import pprint  # python3 -m pip install pprint
import pandas as pd  # python3 -m pip install pandas

URL = "http://192.168.1.220:2224/json"


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
    result1 = pd.json_normalize(respjson)
    pprint(result1)


# invoke the main function
if __name__ == "__main__":
    main()
