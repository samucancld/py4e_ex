import re

def mcw_counter(many,sinput,enc):
    if sinput[len(sinput)-4:] == '.txt':
        fname = sinput
    else:
        fname = sinput + '.txt'
    try:
        many = int(many)
        if enc == '1':
            fhandler = open(fname, encoding='utf-8')
        elif enc == '2':
            fhandler = open(fname)
        else:
            return 'bad input'
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

while True:
    enc=input('type 1 for spanish texts and 2 for english\n> ')
    resultado = mcw_counter(enc = enc, many=input('many>'),sinput=input('file>'))
    print(resultado)
    if resultado != 'bad input':
        break
    else:
        continue 

election = input('do you wanna save this in a file? Y/n\n> ')
if election == '' or re.search('^[yY].*',election):
    sfname = input('file name> ')
    if enc == '1':
        sec_handler = open(sfname,'w',encoding="utf-8")
    elif enc == '2':
        sec_handler = open(sfname,'w')
    sec_handler.write(resultado)