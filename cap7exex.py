

def n_lines_reader(n_lines,fname):
    s_file = ''
    while True:
        try:
            if (fname[-4:]) == '.txt':
               fhand = open(fname)
               break
            else:
                fhand = open(fname+'.txt')
                break
        except:
            print('no se encuentra el archivo')
            return('error')
        
    for line in fhand:
        #line = line.rstrip()
        if n_lines > 0:
            s_file = s_file + line
            n_lines = n_lines - 1
        else:
            break
    return s_file.rstrip()


while True:
    fname = input('file> ')
    while True:
        s_lines = input('lines> ')
        try:
            n_lines = int(s_lines)
            break
        except:
            continue
    result = n_lines_reader(n_lines=n_lines,fname=fname)
    if result != 'error':
        break
    else:
        continue
print(f'The first {n_lines} lines of the file are:\n--------------------------\n{result}\n')




