import os, re
expression = re.compile('^[0-9]+.*txt$')

for a in os.listdir('.'): # For a in every file in the current directory, do:
    if re.match(expression, a): # If file name matches regex expression, delete it.
        os.remove(a)