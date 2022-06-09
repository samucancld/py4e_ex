
fname = input('name> ')
fhand = open(fname)

dow = dict()
low = list()
line = ''

for line in fhand:
    low = line.split()
    for w in low:
        dow[w] = dow.get(w,0)+1

bigcount = None
bigword = None

for k,v in dow.items():
    if bigcount is None or v > bigcount:
        bigcount = v
        bigword = k

print(bigword,bigcount)