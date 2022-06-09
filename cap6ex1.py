#Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.

index = 0
cadena = input('> ')
while index < len(cadena):
    p_let = len(cadena) - 1 - index
    print(cadena[p_let])
    index = index + 1

print('\n')
#sol git
index = len(cadena) - 1
while index >= 0:
    print(cadena[index])
    index = index - 1