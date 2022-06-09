def contador(letter, word):
    count = 0
    for each_letter in word:
        if each_letter == letter:
            count = count + 1
    return count

s_word = input('#word> ')
s_lett = input('#letter> ')
print(contador(word = s_word, letter=s_lett))
print(s_word.count(s_lett))
