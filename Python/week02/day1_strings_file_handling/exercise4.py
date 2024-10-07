# write a program that opens an existing file, reads its contents, and creates
# a new file with a different name, writing the copied contents to the new file

readFile = 'exercise4_sample.txt'
writeFile = 'exercise4_sample_Copy.txt'

myFile = open(readFile, 'r')
dataToCopy = myFile.read()
myFile.close()

myFile2 = open(writeFile, 'w')
myFile2.write(dataToCopy)
myFile2.close()
