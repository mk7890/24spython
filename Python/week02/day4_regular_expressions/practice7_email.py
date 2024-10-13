# match the start of a string
import re

myString = 'purple alice-b@google.com monkey dishwasher'
myPattern = r'\w+@\w+...\w'
myMatch = re.search(myPattern, myString)
if myMatch:
    print(myMatch.group())
    # output: b@google.com
else:
    print('no match')