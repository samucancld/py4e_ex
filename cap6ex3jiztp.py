def contador(sub, phrase):
    count = 0
    largo = len(sub)
    c = 0
    while True:
        try:
            if phrase[c:c+largo] == sub: #and sub != phrase[largo+c:(largo+c) + largo]:
                count = count + 1
            #print(phrase[c:largo+c],count)
            print(phrase[c:c+largo])
            c = c+largo
            print(c)
            if c > len(phrase):
                raise ValueError
        except:
            break
    return count





s_phrase = input('#phrase> ')
s_sub = input('#sub> ')
print(contador(phrase = s_phrase, sub = s_sub))
