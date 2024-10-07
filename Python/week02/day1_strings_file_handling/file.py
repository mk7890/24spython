# file = open('mbox.txt')
# count = 0
#print(file)

# for lines in file:
#     count +=1
# print(f"Number of lines in file : {count}")

#******************************************
#printing all lines beginning with a particular letter

# for myline in file:
#     if myline.startswith('From'):
#         print(myline)

#*******************************************************
#file = open('mbox.txt')

# fileNamePrompt = input("Enter file name to open file: ")
# try:
#     file= open(fileNamePrompt)

#     for myline in file:
#         if myline.startswith('From'):
#             email = myline.find('@')
#             after = myline.find(' ', email)
#             host = myline[email+1: after]
#             print(host)
            
# except:
#     print(f"File not found. You may have entered a non-existent file name")
    
#*******************************************************************************

#WRITING INTO FILES===============================================
file = open('Sample.txt', 'w')  #
text = 'Sample text here'
file.write(text)
file.close
#print(file)
