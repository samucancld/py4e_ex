#Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary.

#Enter file name: mbox-short.txt
#{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
#'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
#'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
#'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
#'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
#'ray@media.berkeley.edu': 1}

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
    print(f'from {k}, {v} messages')




