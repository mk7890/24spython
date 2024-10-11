# Tuples are similar to lists except they can't be changed: --> Immutable

t = ('a', 'b', 'c', 'd', 'e')
num = (1,2,3,4,5)
thisIsAtuple = tuple('hello')
#thisIsAlosAtuple = tuple('moses','ruth')
#

#***** Tuple operations *************************
#   slicing
# print(num[1:3])

#   comparing tuples
tuple1 = (0,5,2,3,4)
tuple2 = (0,2,3,4,5)
compare = tuple1 < tuple2
# print(compare)

#   split function
text = "but soft what light"
words = text.split()
# print(words)
# print(words[1])


#**** Tuple Methods******
#
numbers = (23, 56, 77)
x, y, z = numbers
# print(x)

myIntegers = ['43', '65', '120'] #write a for loop to iterate and sum all the numbers
sum = 0
for myElement in myIntegers:
    sum = sum + int(myElement)
print(f"Sum is : {sum}")

ints = [int(x) for x in myIntegers]
print(sum(ints))