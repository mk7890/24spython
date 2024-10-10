# Dictionaries contain key and values
# keys should not be repeated

# dictionary = {'John':24, 'Peter':36, "Ruth":28, 'John':30} #last duplicate key is ignored
# #print(dictionary)
# for i,j in dictionary.items():
#     print(f"Name: {i},  Age: {j}")

# dictionary methods:
# myDictionary.get(valuePair, default_value)

purse = dict()
purse['tissue'] = 75
purse['candy']= 3
purse['money'] = 12
print(purse)
print(purse['candy'])
purse['candy'] = 7
print(purse)