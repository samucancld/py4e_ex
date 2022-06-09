#Exercise 4: Add code to the above program to figure out who has the most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.

#Enter a file name: mbox-short.txt
#cwen@iupui.edu 5

#Enter a file name: mbox.txt
#zqian@umich.edu 195

max_sender_email = None
max_sender_count = None

while True:
    sinput = input('fname> ')
    if sinput[len(sinput)-4:] == '.txt':
        fname = sinput
    else:
        fname = sinput + '.txt'
    try:
        fhandler = open(fname)
        break
    except:
        print('no existe el archivo')
        continue

lofields = list()
domails = dict()
for line in fhandler:
    if not line.startswith('From '): 
        continue
    lofields = line.split()
    domails[lofields[1]] = domails.get(lofields[1],0) + 1
    #print(domails)

for k,v in domails.items():
    if max_sender_count == None or max_sender_count < v:
        max_sender_email = k
        max_sender_count = v
print(max_sender_email,max_sender_count)