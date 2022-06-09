#Exercise 1: Write a simple program to simulate the operation of the grep command on Unix. Ask the user to enter a regular expression and count the number of lines that matched the regular expression:

#$ python grep.py
#Enter a regular expression: ^Author
#mbox.txt had 1798 lines that matched ^Author

#$ python grep.py
#Enter a regular expression: ^X-
#mbox.txt had 14368 lines that matched ^X-

#$ python grep.py
#Enter a regular expression: java$
#mbox.txt had 4175 lines that matched java$
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
c = 0
regex = input('regex> ')
for each_line in handler:
    each_line = each_line.rstrip()
    if re.search(regex,each_line):
        c = c+1
print(f'{fname} had {c} lines that matched {regex}')


#e = re.findall('^From (\S+@\S+)',c)
#if re.search('^X-\S+:',line):
