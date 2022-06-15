#Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving the document from a URL, (2) displaying up to 3000 characters, and (3) counting the overall number of characters in the document. Don’t worry about the headers for this exercise, simply show the first 3000 characters of the document contents.

import urllib.request, urllib.parse, urllib.error
user_input = input('link> ')
#http://data.pr4e.org/romeo.txt
# http://data.pr4e.org/intro.txt
# http://data.pr4e.org/mbox.txt
handler = urllib.request.urlopen(user_input)

doc = ''
for each_line in handler:
    doc = doc + each_line.decode()

limited_doc = doc[:3000]
print(limited_doc.rstrip())
print(f'showing {len(limited_doc)} over {len(doc)} chars')