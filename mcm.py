max_sender_email = None
max_sender_count = None

while True:
    sinput = input('fname> ')
    if sinput[len(sinput)-4:] == '.txt':
        fname = sinput
    else:
        fname = sinput + '.txt'
    try:
        #fhandler = open(fname,encoding="utf8")
        fhandler = open(fname)
        break
    except:
        print('no existe el archivo')
        continue

lowords = list()
dicwc = dict()
for line in fhandler:
    lowords = line.split()
    for w in lowords:
        dicwc[w] = dicwc.get(w,0) + 1

#print(dicwc)
tmp = list()
#print(dicwc.items())
for k,v in dicwc.items():
    tmp.append((v,k))

tmp.sort(reverse=True)
#tmp = sorted(tmp, reverse=True)

#print(tmp[0:10])

#for i in range(10):
    #print(tmp[i])

#c = 0

for k,v in tmp[0:10]:
    print(f'La palabra "{v}" aparece "{k}" veces')
    #c = c + 1
    #if c == 10: break