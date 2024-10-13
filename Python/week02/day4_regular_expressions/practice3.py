# getting characters given the end character

import re

string = 'piiing'
myPattern = r'..g'

myMatch = re.search(myPattern, string)
if myMatch:
    print(myMatch.group())
else:
    print('match not found')