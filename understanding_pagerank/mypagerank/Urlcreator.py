import urllib.request, urllib.parse, urllib.error
import http
import json
import time
import ssl
import sys

api_key = 42
serviceurl = "http://py4e-data.dr-chuck.net/json?"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


class UrlCreator:

    def __init__(self) -> None:
        pass

    def createUrl(self, address):
        parms = dict()
        parms["address"] = address
        if api_key is not False: parms['key'] = api_key
        url = serviceurl + urllib.parse.urlencode(parms)
        return url