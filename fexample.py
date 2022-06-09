while True:
    fname = input('> ')
    try:
        if (fname[-4:]) == '.txt':
            fhand = open(fname)
        else:
            fhand = open(fname+'.txt')
        break
    except:
        print('no se encuentra el archivo')
        continue
c = 0
for line in fhand:
    if line.startswith('Subject:'):
        c = c + 1
print(f'there were {c} subject lines in {fname}')
