##https://www.youtube.com/watch?v=isOMjkT9fOM
##-- The code for this video is below: --##

# This program will delete all files that match a given regex expression in the current directory.

# The two modules we will need:
import os
import re

expression = re.compile('^empty[0-9]$') # Regex expression for files that start with empty and end with a single digit.
# Alter the above expression to change what files will be deleted.
# For example, change this to:
expression = re.compile('^username_file.*$')
# And this will delete any files that start with username_file.

for a in os.listdir('.'): # For a in every file in the current directory, do:
    if re.match(expression, a): # If file name matches regex expression, delete it.
        os.remove(a)

# Done.
# :D