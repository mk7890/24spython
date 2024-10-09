# a set is a collection of unique data. duplicate data is not allowed
student_info = {12, 'John', 'John'}
#print(student_info)

# creating an empty set
myEmpthSet = set()

# Adding items to a set

numbers = {23,3,5,90}
numbers.add(10)
#print(numbers)

# updating items in a set

new_nums = {1,4,6}
numbers.update(new_nums)
#print(numbers)

# removing elements from a set
numbers.discard(90)
#print(numbers)

# looping items in a set
for number in numbers:
    #print(number)
    pass
    
#finding the number of elements in a set
setLength = len(numbers)
#print(setLength)

# set operations ********
#******** union of two sets*******
setA = {1,3,5}
setB = {1,2,4}
unionAB = setA | setB
#print(unionAB)

#******** intersection of two sets ****
intersectionAB = setA & setB
# print(intersectionAB)

#********* difference between sets ****
differenceAB = setA - setB
# print(differenceAB)

#********* symmetric difference between sets ***->without common elements
symmetricAB = setA ^ setB
# print(symmetricAB)

#******* Check if two sets are equal
setC = {1,3,5}
setD = {3,5,1}
if setC == setD:
    print(f"setC and setD are equal")
else:
    print(f"setC and setD are not equal")
