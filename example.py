#

#mail = input('> ')
mail = 'From samuel5848@gmail.com Sat Jan 5 09:14:16 2008'

arroba = mail.find('@')
print(arroba)
espacio = mail.find(' ',arroba)
casilla = mail[arroba+1:espacio]
print(casilla)