from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

lista = list()
c = 0
tags = soup('span')
for tag in tags:
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    lista.append(int(tag.contents[0]))
    c = c + 1
    #print('Attrs:', tag.attrs)
print('Count',c)
print('Sum',sum(lista))

#http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
#http://py4e-data.dr-chuck.net/comments_1576861.html