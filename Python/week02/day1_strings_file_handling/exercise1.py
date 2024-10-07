#This program counts the number of words in sentence entered by the user

mySentence = input("Write a Sentence: ") #prompt the user to write a sentence

mySentenceList = mySentence.split() #use the split function to create a list containg every word in the sentence excluding spaces
numWords = len(mySentenceList) #use the len function to get the words in the list 
print(f"Your sentence has {numWords} words") #print the number of words in the sentence