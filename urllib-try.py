import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

#for each_line in fhand:
    #print(each_line.decode().strip())


counts = dict()
for each_line in fhand:
    words = each_line.decode().split()
    for word in words:
        counts[word]=counts.get(word,0)+1
print(counts)

lot = list()
for k,v in counts.items():
    lot.append((v,k))

lot.sort(reverse=True)

for each_tuple in lot:
    print(f'The word {each_tuple[1]} appear {each_tuple[0]} times')



print(lot)
