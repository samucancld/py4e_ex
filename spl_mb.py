fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    #print(f'{words[2]}')
    casilla = words[1]
    casillas = casilla.split('@')
    print(f'message from {casillas[1]} on {words[2]}')
