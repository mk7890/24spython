# Write a program that opens a text file and iterates through 
# each line using a for loop printing each line separately

myFile = open('exercise5_sample.txt') #open text file document exercise5_sample.txt and assign it to handle myFile
#use a for loop to read through every line in exercise5_sample.txt
for lineToPrint in myFile: #create variable lineToPrint to store content in every line of exercise5_sample.txt when iterating
    lineToPrint = lineToPrint.rstrip() #use rstrip function to get rid of whitespace characters to avoid line skipping
    print(lineToPrint) #print lines sequencially in exercise5_sample.txt in every iteration
    