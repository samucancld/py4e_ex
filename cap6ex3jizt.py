def contador(sub, phrase):
    count = 0
    largo = len(sub)
    c = 0
    for each_letter in phrase:
        if phrase[c:largo+c] == sub and sub != phrase[largo+c:(largo+c) + largo]:
            count = count + 1
        #print(phrase[c:largo+c],count)
        print(phrase[c:largo+c],phrase[largo+c:(largo+c) + largo],count)
        c = c+1
    return count

s_phrase = input('#phrase> ')
s_sub = input('#sub> ')
print(contador(phrase = s_phrase, sub = s_sub))
