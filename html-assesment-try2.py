import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

actual_link = input('Enter URL:')
count = int(input('Enter count: '))
init_pos = int(input('Enter position: '))
#http://py4e-data.dr-chuck.net/known_by_Hania.html
print(actual_link)
for i in range(count):
    pos = init_pos
    html = urlopen(actual_link, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    links = []
    tags = soup('a')
    for tag in tags:
        if pos < 1 : break
        links.append(tag.get('href', None))
        pos = pos - 1
    actual_link = links[-1]
    print('Retrieving:',actual_link)
