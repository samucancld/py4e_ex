import re
#con regex
hand = open ('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)
print('------------------------------------------')
#sin regex
shand = open('mbox-short.txt')
for sline in shand:
    sline = sline.rstrip()
    if sline.find('From:') >= 0:
        print(sline)
