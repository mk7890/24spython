# one i or more for as many as possible
import re

string = 'pijiig'
pattern = r'i+'
match = re.search(pattern, string)
if match:
    print(match.group())
else:
    print('no match')