#Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt

#Write a program that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.

fhandler = open('words.txt')
lowords = list()
dowords = dict()
for line in fhandler:
    lowords = line.split()
    for w in lowords:
        dowords[w] = 0

def is_in_words_dot_txt(word):
    if word in dowords:
        return 'YES IT IS'
    else:
        return 'NO IS NOT'


while True:
    sinput = input('> ')
    if sinput == '#done#':
        break
    else:
        print(is_in_words_dot_txt(sinput))
