#Exercise 2: This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the “From” line by finding the time string and then splitting that string into parts using the colon character. Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

#python timeofday.py
#Enter a file name: mbox-short.txt
#04 3
#06 1
##07 1
#09 2
#10 3
#11 6
#14 1
#15 2
#16 4
#17 2
#18 1
#19 1

while True:
    inp = input('file> ')
    try:
        #print('debug',inp[-4:])
        if inp[-4:] == '.txt':
            handler = open(inp)
        else:
            handler = open(inp+'.txt')
        break
    except:
        continue


dict_of_hs = dict()
for each_line in handler:
    if not each_line.startswith('From ') or len(each_line) < 6:
        continue
    lof = each_line.split()
    hora = lof[5].split(':')[0]
    dict_of_hs[hora] = dict_of_hs.get(hora,0) + 1

lotup = list()

for k,v in dict_of_hs.items():
    lotup.append((k,v))

lotup.sort()

#for k,v in dict_of_hs.items():
#    lotup.append((v,k))

#lotup.sort(reverse=True)

#for k,v in lotup:
    #print(v,k)


#print(lof)
#print(hora)
#print(dict_of_hs)

for k,v in lotup:
    print(k,v)


print(lotup)

