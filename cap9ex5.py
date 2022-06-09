#Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.

#python schoolcount.py
#Enter a file name: mbox-short.txt
#{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
#'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

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
    arroba = lofields[1].find('@')
    #print(lofields[1],arroba)
    domails[lofields[1][arroba:]] = domails.get(lofields[1][arroba:],0) + 1
    #print(domails)

for k,v in domails.items():
    #arroba = k.find('@')
    #print(arroba)
    print(f'from {k}, {v} messages')