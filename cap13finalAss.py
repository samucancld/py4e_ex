import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
   
    url = serviceurl + urllib.parse.urlencode(parms)
    
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    
    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        continue

    print(json.dumps(js, indent=4))
    place_id = js['results'][0]["place_id"]
    print(place_id)