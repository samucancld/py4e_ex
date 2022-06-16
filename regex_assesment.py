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
list_of_inums = list()
#for each line in the file
for each_line in handler:
    #remove the \n at the end of the line
    each_line.rstrip()
    #save the return of re.findall, could be a blank list or a list with the value in str
    #the regex mean maatch everything that are numbers from 0 to 9, extracting just the numbers
    list_of_snums = re.findall('([0-9]+)',each_line)
    #make sure that in the line are at least 1 coincidence
    if len(list_of_snums) < 1:
         continue
    #append the numbers to the list of vallues typing it to integer
    for each_snum in list_of_snums:
        list_of_inums.append(int(each_snum))
#print the sum
print(sum(list_of_inums))