# write a program that opens an existing file, reads its contents, and creates
# a new file with a different name, writing the copied contents to the new file

readFile = 'exercise4_sample.txt' #assign a original string name to variable readFile
writeFile = 'exercise4_sample_Copy.txt' #assign copied string name to variable writeFile
#code below opens, reads, and copies contents of exercise4_sample.txt document to variable dataToCopy
myFile = open(readFile, 'r') #open exercise4_sample.txt file document within same directory as python code file
dataToCopy = myFile.read() #use built-in read function to read and copy data to variable dataToCopy
myFile.close() #close exercise4_sample.txt file 
#code below creates a new text file document 'exercise4_sample_copy.txt', writes content from exercise4_sample.txt
myFile2 = open(writeFile, 'w') #open exercise4_sample_copy.txt with write mode enabled, otherwise create it if it doesn't exist
myFile2.write(dataToCopy) #use built-in write function to copy exercise4_sample.txt data stored in variable dataToCopy to new file document
myFile2.close() #close exercise4_sample_copy.txt
