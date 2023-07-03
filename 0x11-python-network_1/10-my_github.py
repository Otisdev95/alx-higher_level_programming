#!/usr/bin/python3
"""
    Script that takes your GitHub credentials (username
    and password) and uses the GitHub API to display your id
"""
import sys
import requests


if __name__ == '__main__':
    url = "https://api.github.com/user"
    response = requests.get(
        url, auth=requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    res_dict = response.json()
    print(res_dict.get('id'))
