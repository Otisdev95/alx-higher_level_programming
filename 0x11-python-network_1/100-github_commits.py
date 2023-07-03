#!/usr/bin/python3
"""
    Script that takes 2 arguments in order to solve this challenge.
"""
import sys
import requests


url = 'https://api.github.com/repos/{}/{}/commits'.format(
    sys.argv[2], sys.argv[1])
try:
    response = requests.get(url)
    res_dict = response.json()
    for i in range(0, 10):
        print("{}: {}".format(res_dict[i].get('sha'), res_dict[i].get(
            'commit').get('author').get('name')))
        except Exception:
            pass
