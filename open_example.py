fhand = open('mbox.txt','r')
print(fhand)

#for line in fhand:
    #line = line.rstrip()
    #if line.startswith('From:'):
        #print(line)

print('/n')

for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        if 'iupui' in line:
            print(line)



#xfile = ''
#for lines in fhand:
    #xfile = xfile + lines

#print(xfile)

#yfile = fhand.read()
#print(yfile)