#This program checks whether two words or phrases are anagrams or each other
#Anagram-> word or phrase made by rearranging letters

print(f"This program checks whether two words or phrases are anagrams or each other")
print(f"Anagram examples: listen - silent; bear - bare; wolf - flow; aunt - tuna")
firstWord = input("Enter the first word/phrase: ")
secondWord = input("Enter the second word/phrase: ")

firstWordLength = len(firstWord)
secondWordLength = len(secondWord)

if firstWordLength == secondWordLength:
    #line below uses the sorted() function to rearrange the letters in default alphbetical order and compare them
    if sorted(firstWord)==sorted(secondWord): 
        print(f"{firstWord} and {secondWord} are anagrams")
else:
    print(f"{firstWord} and {secondWord} are not anagrams")
    