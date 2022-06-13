import urllib.request, urllib.parse, urllib.error
import re
fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.html')

for line in fhand:
    decoded_line = line.decode().strip()
    print(line.decode().strip())
    if len(re.findall('href="([\S]*)"',decoded_line)) != 1:
        continue
    link = re.findall('href="([\S]*)"',decoded_line)
print('\n---------------------------------\n')
print(link)
strlink = link[0]
print(strlink)
line = ''
fhand.close()
fhand = urllib.request.urlopen(strlink)
print('\n---------------------------------\n')
for line in fhand:
    decoded_line = line.decode().strip()
    print(line.decode().strip())
    if len(re.findall('href="([\S]*)"',decoded_line)) != 1:
        continue
    link = re.findall('href="([\S]*)"',decoded_line)
print('\n---------------------------------\n')
print(link)

