from turtle import position
import urllib.request, urllib.parse, urllib.error
import re

# lolinks = list()

count = int(input('count> '))
pos = int(input('pos> ')) - 1
actual_link = 'http://py4e-data.dr-chuck.net/known_by_Hania.html'
print(actual_link)
while count > 0:
    fhand = urllib.request.urlopen(actual_link)
    links = []
    for line in fhand:
        decoded_line = line.decode().strip()
        if len(re.findall('href="([\S]*)"',decoded_line)) < 1:
            continue
        links.append(re.findall('href="([\S]*)"',decoded_line))
    actual_link = str(links[pos])
    actual_link = actual_link[2:-2]
    ifrom = actual_link.find('known_by_')
    print(actual_link.strip()[ifrom+9:-5])
    fhand.close()
    count = count - 1

#  http://py4e-data.dr-chuck.net/known_by_Fikret.html
# http://py4e-data.dr-chuck.net/known_by_Hania.html