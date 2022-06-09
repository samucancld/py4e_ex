#Exercise 2: Write a program to look for lines of the form:

#New Revision: 39772
#Extract the number from each of the lines using a regular expression and the findall() method. Compute the average of the numbers and print out the average as an integer.

#Enter file:mbox.txt
#38549

#Enter file:mbox-short.txt
#39756

import re
while True:
    fname = input('fname> ')
    try:
        #print(fname[-4:])
        if fname[-4:] == '.txt':
            handler = open(fname)
        else:
            handler = open(fname+'.txt')
        break
    except:
        print("file doesn't found")
        continue

list_of_values = list()
c = 0
for each_line in handler:
    each_line.rstrip()
    list_of_1_match = re.findall('^New Revision: ([0-9]+)',each_line)
    if len(list_of_1_match) != 1:
        continue
    list_of_values.append(int(list_of_1_match[0]))
    c = c + 1
print(int(sum(list_of_values)/c))