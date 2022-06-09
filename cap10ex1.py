#Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.

#After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.

#Sample Line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

#Enter a file name: mbox-short.txt
#cwen@iupui.edu 5

#Enter a file name: mbox.txt
#zqian@umich.edu 195
while True:
    inp = input('file> ')
    try:
        #print('debug',inp[-4:])
        if inp[-4:] == '.txt':
            handler = open(inp)
        else:
            handler = open(inp+'.txt')
        break
    except:
        continue
unordered_dictionary = dict()
addresses = list()
for each_line in handler:
    if not each_line.startswith('From ') or len(each_line) < 3:
        continue
    splitted_line = each_line.split()
    #addresses.append(splitted_line[1])
    unordered_dictionary[splitted_line[1]] = unordered_dictionary.get(splitted_line[1],0) + 1

#print('debug:',unordered_dictionary)

lotup = list()
lotup[:] = unordered_dictionary.items()

reverse_lotup = list()

for k,v in lotup:
    reverse_lotup.append((v,k))

reverse_lotup.sort(reverse=True)

#for k,v in reverse_lotup:
#    print('debug:',v,k)

#print('debug',reverse_lotup)

print(reverse_lotup[0][1],reverse_lotup[0][0])




