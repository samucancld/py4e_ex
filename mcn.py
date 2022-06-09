ccc = dict()
name = ''
while True:
    name = input('name>')
    if not name in ccc and name != 'done':
        ccc[name] = 1
    elif name == 'done':
        break
    else: 
        ccc[name]=ccc[name]+1

print(ccc)

