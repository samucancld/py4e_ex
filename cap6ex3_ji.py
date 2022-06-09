def contador(sub, phrase):
    count = 0
    largo = len(sub)
    c = 0
    for each_letter in phrase:
        if phrase[c:largo+c] == sub: #and sub != word[cont:len(sub)]:
            count = count + 1
        print(phrase[c:largo+c],count)
        c = c+1
    return count

s_phrase = input('#phrase> ')
s_sub = input('#sub> ')
print(contador(phrase = s_phrase, sub = s_sub))
#print(s_word.count(s_lett))