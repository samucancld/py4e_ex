# Exercise 5: (Advanced) Change the socket program so that it only shows data after the headers and a blank line have been received. Remember that recv receives characters (newlines and all), not lines.

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))

cmd = 'GET http://data.pr4e.org/intro.txt HTTP/1.0\r\n\r\n'.encode()

mysock.send(cmd)

doc = ''


while True:
    data = mysock.recv(512)
    if len(data)< 1:
        break
    # print(data.decode())
    doc = doc + data.decode()
mysock.close()

#print(doc)
#doc = doc.rstrip()
end_of_header = doc.find('\r\n\r\n')
print(doc[end_of_header:].strip())
