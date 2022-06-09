#Exercise 2: Write a program to look for lines of the form:

#New Revision: 39772
#Extract the number from each of the lines using a regular expression and the findall() method. Compute the average of the numbers and print out the average as an integer.

#Enter file:mbox.txt
#38549

#Enter file:mbox-short.txt
#39756

#import 'r'egular 'e'xpressions library
import re
#infinite loop
while True:
    #prompt for the name
    fname = input('fname> ')
    #try to open a file with the given name
    try:
        #add extension if necessary
        if fname[-4:] == '.txt':
            handler = open(fname)
        else:
            handler = open(fname+'.txt')
        #if the file have been succesfully open, break the loop
        break
    #catch the error of open a file that doesnt exist
    except:
        print("file doesn't found")
        continue
#initializing list of valuable values
list_of_values = list()
#initializing counter in 0
c = 0
#for each line in the file
sec_handler = open('revisions.txt','w')
for each_line in handler:
    #remove the \n at the end of the line
    each_line.rstrip()
    #save the return of re.findall, could be a blank list or a list with the value in str
    #the regex mean maatch everything that begin with 'New Revision: ' followed by 1 or
    #more characters that are numbers from 0 to 9, extracting just the numbers
    list_of_1_match = re.findall('^New Revision: ([0-9]+)',each_line)
    #make sure that at the coincidence is just 1 (cant be more numbers)
    if len(list_of_1_match) != 1:
        continue
    #append the number to the list of vallues typing it to integer
    list_of_values.append(int(list_of_1_match[0]))
    sec_handler.write(list_of_1_match[0]+'\n')
    #increase the counter
    c = c + 1
#print the average
#guard
if c > 0:
    print(int(sum(list_of_values)/c))