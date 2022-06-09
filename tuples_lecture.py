lotosingers = list()
dosingers = {'x':'miley','w':'selena','t':'lana'}
print('dict ',dosingers)
lotosingers[:] = dosingers.items()
print('list ', lotosingers)
#sortedlts = sorted(lotosingers)
#lotosingers.sort()
#print('ord list', sortedlts)
#print(lotosingers)
reverse_lot = list()
for k,v in lotosingers:
    reverse_lot.append((v,k))

print(reverse_lot)
reverse_lot.sort()
#reverse_lot = sorted(reverse_lot, reverse=True)
print(reverse_lot)
