abc = 'With three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])

for w in stuff:
    print(w)

ghi = list()
new_str = ''
for ch in stuff[1]:
    if ch == 'e':
        ghi.append('x')
    else: 
        ghi.append(ch)
print(ghi)
for l in ghi:
    new_str = new_str + l
print(new_str)

stuff[1] = new_str
n_abc = ''
for pal in stuff:
    n_abc = n_abc + pal + ' '
print(n_abc)




