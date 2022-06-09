#Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:
#X-DSPAM-Confidence: 0.8475
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
tot = 0.0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        s_num = line[line.find(':')+1:]    
        f_num = float(s_num)
        tot = tot + f_num
        c = c + 1
print(tot,c,tot/c)



