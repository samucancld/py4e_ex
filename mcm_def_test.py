def mcw_counter(many,sinput):
    if sinput[len(sinput)-4:] == '.txt':
        fname = sinput
    else:
        fname = sinput + '.txt'
    try:
        many = int(many)
        fhandler = open(fname)
    except:
        return 'bad input'
    lowords = list()
    dicwc = dict()
    for line in fhandler:
        lowords = line.split()
        for w in lowords:
            dicwc[w] = dicwc.get(w,0) + 1

    mcw = list()

    for k,v in dicwc.items():
        mcw.append((v,k))

    mcw.sort(reverse=True)

    finalstr = ''
    for k,v in mcw[0:many]:
        #print(f'La palabra "{v}" aparece "{k}" veces')
        finalstr = finalstr + f'La palabra "{v}" aparece "{k}" veces\n'
    finalstr = finalstr.rstrip()
    return finalstr