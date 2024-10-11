# Write a function to create a new set that contains the identical items from 
# the two given sets.

# return the identical elements from the two given sets
# for inputs with sets {1,2,3,4} and {3,4,5,6} the return value should be
# {3,4} or {4,3}

setA = {1,2,3,4}
setB = {3,4,5,6}

def newSet():
    setC = setA & setB
    return setC
print(newSet())
