#Exercise 2: Change your socket program so that it counts the number of characters it has received and stops displaying any text after it has shown 3000 characters. The program should retrieve the entire document and count the total number of characters and display the count of the number of characters at the end of the document.

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

user_input = input('link> ')
list_of_comp = user_input.split('/')
#print('Debug:',list_of_comp)

mysock.connect((list_of_comp[2], 80))
mysock.send((f'GET {user_input} HTTP/1.0\r\n\r\n').encode())

doc = ''
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    doc = doc + data.decode()
mysock.close()

end_of_header = doc.find('\r\n\r\n')
limited_data = doc[end_of_header:end_of_header+3000]

print(f'Primeros 3000 caracteres:\n-----------------------------------\n{limited_data.strip()}')
print('-----------------------------------')
print(f'showed {len(limited_data)} over {len(doc)} chars!')


#TESTED WITH http://data.pr4e.org/intro.txt