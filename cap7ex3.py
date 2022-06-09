#Exercise 3: Sometimes when programmers get bored or want to have a bit of fun, they add a harmless Easter Egg to their program. Modify the program that prompts the user for the file name so that it prints a funny message when the user types in the exact file name “na na boo boo”. The program should behave normally for all other files which exist and don’t exist. Here is a sample execution of the program:

while True:
    fname = input('> ')
    try:
        if (fname[-4:]) == '.txt':
            fhand = open(fname,'r')
        else:
            fhand = open(fname+'.txt','r')
        break
    except:
        if fname == 'na na boo boo':
            print("NA NA BOO BOO TO YOU - You have been punk'd!")    
        else:
            print('no se encuentra el archivo')
        continue
c = 0
tot = 0.0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        s_num = line[line.find(':')+1:]    
        f_num = float(s_num)
        tot = tot + f_num
        c = c + 1
print(tot,c,tot/c)



