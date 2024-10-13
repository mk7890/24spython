import re

# make a pattern to search for a word that starts with 'H'
myString = 'Hello World. Python programming is fun'
pattern = r'^H'
match = re.search(pattern, myString)

if match:
    print('Found ', match.group())
    print('start index ', match.start())
    print('end index ', match.end)
else:
    print('Not found')