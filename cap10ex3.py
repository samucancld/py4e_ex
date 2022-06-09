#Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.

#Fun fact: The word “tuple” comes from the names given to sequences of numbers of varying lengths: single, double, triple, quadruple, quintuple, sextuple, septuple, etc.↩︎

#Python does not translate the syntax literally. For example, if you try this with a dictionary, it will not work as you might expect.↩︎

while True:
    inp = input('file> ')
    try:
        #print('debug',inp[-4:])
        if inp[-4:] == '.txt':
            handler = open(inp)
        else:
            handler = open(inp+'.txt',encoding="utf-8")
        break
    except:
        continue

c = 0
abcetc = 'abcdefghijklmnñopqrstuvwxyz'
letters = list()
dict_counter = dict()
for each_letter in abcetc:
    letters.append(each_letter)
for each_line in handler:
    each_line = each_line.lower()
    for each_letter in each_line:
        if each_letter in letters:
            dict_counter[each_letter] = dict_counter.get(each_letter,0) + 1
            c = c + 1

list_counter = list()
for k,v in dict_counter.items():
    list_counter.append((v,k))

list_counter.sort(reverse=True)
#print(debug:,list_counter)

for k,v in list_counter:
    print(f'The letter "{v}" have a frecuency of {str((k/c)*100)[:5]}% in this text.')
