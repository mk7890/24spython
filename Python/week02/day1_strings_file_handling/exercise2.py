#This program checks whether two words or phrases are anagrams or each other
#Anagram-> word or phrase made by rearranging letters

print(f"This program checks whether two words or phrases are anagrams or each other")
print(f"Anagram examples: listen - silent; bear - bare; wolf - flow; aunt - tuna")
firstWord = input("Enter the first word/phrase: ") #prompt user to enter a phrase and store it in variable
secondWord = input("Enter the second word/phrase: ") #prompt user to enter a phrase and store it in variable

firstWordLength = len(firstWord) #use length function to store length of firstword in variable
secondWordLength = len(secondWord) #use length function to store length of secondword in variable

if firstWordLength == secondWordLength: # code executes only if equal lengths of words entered
    #line below uses the sorted() function to rearrange the letters in default alphbetical order and compare them
    if sorted(firstWord)==sorted(secondWord): #if sorted phrases are the same code below executes
        print(f"{firstWord} and {secondWord} are anagrams")
else: #code executes when words lengths and letter repetition times fail
    print(f"{firstWord} and {secondWord} are not anagrams")
    