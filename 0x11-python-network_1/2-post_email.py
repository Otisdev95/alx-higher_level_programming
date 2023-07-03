#!/usr/bin/python3
"""
    Script that takes in a URL and an email, sends a POST request to the
    passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    email = urllib.parse.urlencode(value)
    email = email.encode('ascii')
    url_req = urllib.request.Request(url, email)

    with urllib.request.urlopen(url_req) as response:
        url_res = response.read()
    output = url_res.decode('utf-8')
    print(output)
