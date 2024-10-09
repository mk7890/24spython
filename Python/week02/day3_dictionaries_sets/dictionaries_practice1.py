"""
    Write a program that reads the words in words.txt and stores them as keys 
    in a dictionary. It doesn’t matter what the values are. Then you can use 
    the in operator as a fast way to check whether a string is in the dictionary.
"""
file = open('words.txt', 'r')
d = dict()

for line in file:
    words = line.split()
    for word in words:
        if word not in d:
            d[word] = 1
        else:
            d[word] +=1
file.close()   
print(d)


