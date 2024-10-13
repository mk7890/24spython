# zero or more whitespace
import re

myString = 'xx1 2   3xx'
myPattern = r'\d\s*\d\s*\d'
myMatch = re.search(myPattern, myString)
if myMatch:
    print(myMatch.group())
else:
    print('no match')