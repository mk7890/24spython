#for loop that prints a pattern of stars like a triangle
    
# number of rows of the tringle
rows = int(input("Enter the number of rows of your triangle: "))
for i in range(0, rows):
    # nested loop for each column
    for j in range(0, i + 1):
        # print star
        print("*", end=' ')
    # new line after each row
    print("\r")