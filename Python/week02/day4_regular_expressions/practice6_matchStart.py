# match the start of a string
import re

myString = 'foobar'
myPattern = r'^f\w+'
myMatch = re.search(myPattern, myString)
if myMatch:
    print(myMatch.group())
else:
    print('no match')