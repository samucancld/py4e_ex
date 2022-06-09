ccc = dict()
name = ''
while True:
    name = input('name>')
    if name == 'done': break
    ccc[name] = ccc.get(name, 0) + 1
print(ccc)

