# the clown ran after the car adn the car ran into the tent adn the tent fell down on the clown and the car

low = list()
line = input('>')
dow = dict()

low = line.split()

for w in low:
    dow[w] = dow.get(w,0) + 1

print(low)

for key in dow:
    print(key, dow[key])

print(dow)
