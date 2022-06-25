# Exercise 1: Change either geojson.py or geoxml.py to print out the two-character country code from the retrieved data. Add error checking so your program does not traceback if the country code is not there. Once you have it working, search for “Atlantic Ocean” and make sure it can handle locations that are not in any country.

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    #si no tenes una api_key de google usas la copia de la api que aloja dr chuck, con una api key de valor 42
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    #parms es un diccionario con key address y value la direccion inputeada y con key key y value 42 o la api key que tengamos
    # print('Debug parms:',parms)
    # print('Debug parms parseado:',urllib.parse.urlencode(parms))
    # print('Debug serviceurl:',serviceurl)
    url = serviceurl + urllib.parse.urlencode(parms)
    # print('Debug url(serviceurl+parsedparms)', url)
    #handling the request
    uh = urllib.request.urlopen(url, context=ctx)
    #decoding utf-8 into a unicode string
    data = uh.read().decode()
    #print('Retrieved', len(data), 'characters')
    #print('Debug data',data)

    try:
        # parsing json data into a dictionary with two keys, one called status with a value of OK and one called results with a list of dictionaries 
        js = json.loads(data)
        #print('Debug js(parsed data):',js)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        # print(data)
        continue

    #print(json.dumps(js, indent=4))
    #print('Debug pos 0:',js['results'][0])
    # pos 0 is used because is one single result, meaning the google api just response with ONE result
    lat = js['results'][0]['geometry']['location']['lat']

    lng = js['results'][0]['geometry']['location']['lng']

    try:
        depto = js['results'][0]['address_components'][1]['short_name']
        splited_depto = depto.split()
        #print('Debug splitted depto:',splited_depto)
        splited_depto.pop()
        #print('Debug splited_depto with pop',splited_depto)
        joined_depto = ' '.join(splited_depto)
        #print('Debug joined_depto:',joined_depto)
        print('Depto: ', joined_depto)
    except:
        print("==== doesn't belong to any department ====")


    location = js['results'][0]['formatted_address']

    #######################################

    try:
        tw_ch_ccode = js['results'][0]['address_components'][3]['short_name']
        #print('Debug two char code:',tw_ch_ccode)
        print('two char code:',tw_ch_ccode)
    except:
        print('==== no two char country code ====')
    #######################################

    print('lat', lat, 'lng', lng)

    
    print(location)
