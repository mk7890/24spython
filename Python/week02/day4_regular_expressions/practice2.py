# Find digit character in example below
import re
string = 'p123g'
phoneNumber = '123-456-7890'
pattern = r'\d{3}-\d{3}-\d{4}'
match = re.search(pattern, phoneNumber)

if match:
    print('digit characters found', match.group())
else:
    print('digit characters not found')
    


