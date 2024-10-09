# looping through a dictionary

counts = {'chuck':1, 'annie':33, 'jan':100}

#************************************************
for keys in counts:
    print(keys, counts[keys])

print('\n')

for item in counts:
    if counts[item] > 10:
        print(item, counts[item])

#****************************************       
lst = list(counts.keys())
lst2 = list(counts.values())
lst.sort()
lst2.sort()

for i in lst:
    print(counts, i)
print()
for j in lst2:
    print(counts, j)
print()
for n in lst:
    print(n, counts[n])
