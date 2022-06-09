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
    if not line.startswith('From:'): 
        continue
    lofields = line.split()
    domails[lofields[1]] = domails.get(lofields[1],0) + 1
    #print(domails)

for k,v in domails.items():
    print(f'from {k}, {v} messages')