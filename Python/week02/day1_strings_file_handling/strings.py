#text = "Hello Python"
#myFruit = 'banana'

# print(text[-1])   prints the character at the last index
# print(len(text))  prints the length of the string
# print(text[index:index])  string slicing

# count = 0

# for letter in text:
#     if letter == 'o':
#         count +=1
# print(count)

# checkCharacter = 'p' in text  # in operator is case sensitive
# print(checkCharacter)


# if myFruit < 'apple':
#     print(f"the fruit {myFruit} comes before apple")
# elif myFruit > 'apple':
#     print(f"the fruit {myFruit} comes after apple")
# else:
#     print(f"both fruits are {myFruit}")

# print(text.upper())
# print(text.lower())

#*************************************************************************

# text = 'mangoes are very sweet' # ->> mango is SWEET
# myWord = 'sweet'
# if myWord in text:
#     myWord = myWord.upper()
#     print(f"mango is {myWord}")

# result = text.index('sweet')
# resultWord = text[result:]

# print(result)
# print(resultWord)
# print(f"{text[:result-1]} {resultWord.upper()}")

#*************************************************************************
myEmail = 'my email address is mugambimoses2@gmail.com'
email = myEmail.find('@')
after = myEmail.find(' ', email)
host = myEmail[email+1:after]

print(host)



