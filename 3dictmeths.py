dosingers = {'miley':10, 'ariana':9,'lorde':8}

losnames = dosingers.keys()
print('names',losnames)

losscores = dosingers.values()
print('scores',losscores)

lotsingers = dosingers.items()
print('list of tuples',lotsingers)

for k,v in dosingers.items():
    print(k,v)