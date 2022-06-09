def contador(letter, word):
    count = 0
    cont = 1
    for each_letter in word:
        try:
            if each_letter == letter and each_letter != word[cont]:
                count = count + 1
            cont = cont + 1
            print(each_letter,word[cont-1],count)

        except:
            if each_letter == letter:
                count = count + 1
            print(each_letter,' ',count)
    return count

s_word = input('#word> ')
s_lett = input('#letter> ')
print(contador(word = s_word, letter=s_lett))
print(s_word.count(s_lett))