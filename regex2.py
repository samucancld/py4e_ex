#sin regex

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From:'):
        ''
        #print(line)
#hand.close()
#con regex
print('--------------------------------------------------------------')

import re
hand = open ('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        ''
        #print(line)
# ^  = startswith
# .  = anything
# *  = many times
# \S = non-whitespace char
# +  = 1+ times
# [] = inside is what we want 4 a single char
import re
hand = open ('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    #if re.search('^X.*:', line):
    if re.search('^X-\S+:',line):
        print(line)
