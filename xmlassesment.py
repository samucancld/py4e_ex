import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('Enter location: ')
    if len(url) < 1: break
    print('Retrieving', url)
    urlhandler = urllib.request.urlopen(url, context=ctx)

    data = urlhandler.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    tree = ET.fromstring(data)

    comments = tree.findall('comments')

    cuenta = 0
    for each_comment in comments[0]:
        # print(each_comment)
        cuenta = cuenta + int(each_comment.find('count').text)
    print(cuenta)


#http://py4e-data.dr-chuck.net/comments_1576863.xml