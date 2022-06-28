import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys
from Urlcreator import *
from Urlopener import *

conn = sqlite3.connect('mygeodata.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')


fh = open("wherearg.data")
count = 0
for line in fh:
    if count > 200 :
        print('Retrieved 200 locations, restart to retrieve more')
        break

    address = line.strip()
    print('')
    
    cur.execute("SELECT geodata FROM Locations WHERE address= ?", (memoryview(address.encode()), ))

    try:
        data = cur.fetchone()[0]
        print("Found in database ",address)
        continue
    except:
        pass

    my_url_creator = UrlCreator()
    url = my_url_creator.createUrl(address=address)

    print(url)

    my_url_opener = UrlOpener()
    data = my_url_opener.openURL(url)
    count = count + 1

    print('Debug data retrieved from URL:\n==========================',data)

    try:
        jsondata = json.loads(data)
    except:
        continue

    print('Debug data parsed on json:\n==========================',jsondata)

    if 'status' not in jsondata or (jsondata['status'] != 'OK' and jsondata['status'] != 'ZERO_RESULTS') :
        print('==== Failure To Retrieve ====')
        break

    cur.execute('''INSERT INTO Locations (address, geodata) VALUES ( ?, ? )''', (memoryview(address.encode()), memoryview(data.encode()) ) )
    conn.commit()
    if count % 10 == 0 :
        print('Pausing for a bit...')
        time.sleep(5)

print("Run geodump.py to read the data from the database so you can vizualize it on a map.")
