#Exercise 2: Write a program to look for lines of the form:

#New Revision: 39772
#Extract the number from each of the lines using a regular expression and the findall() method. Compute the average of the numbers and print out the average as an integer.

#Enter file:mbox.txt
#38549

#Enter file:mbox-short.txt
#39756

import re
print('name without extension = utf-8\nname with extension = def')
while True:
    fname = input('fname> ')
    try:
        #print(fname[-4:])
        if fname[-4:] == '.txt':
            handler = open(fname)
        else:
            handler = open(fname+'.txt',encoding='utf-8')
        break
    except:
        print("file doesn't found")
        continue

tmp = list()
c = 0
for each_line in handler:
    tmp.append(re.findall('^New Revision: ([0-9]+)',each_line))
    if len(tmp[-1]) == 0:
        tmp.pop()
    else:
        c = c+1
    #print(tmp)
    #itmp = int(tmp[0])
    #print(itmp)
    #if itmp > 0:
        #lonums.append(itmp)
        #print(greped_line)
        #lonums.append(int(greped_line))
    #print(lonums)
maxi = int(max(tmp)[0])
print(maxi)

print(maxi/c)