#Exercise 1: Write a program to read through a file and print the contents of the file (line by line) all in upper case. Executing the program will look as follows:

while True:
    fname = input('> ')
    try:
        if (fname[-4:]) == '.txt':
            fhand = open(fname)
        else:
            fhand = open(fname+'.txt')
        break
    except:
        print('no se encuentra el archivo')
        continue
c = 0
for line in fhand:
    print(line.rstrip().upper())
