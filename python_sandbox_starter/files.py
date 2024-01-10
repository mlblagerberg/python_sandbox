# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile = open('myfile.txt', 'w') # mode is to write which is the 'w'

# Get some info on file you just created
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.write('I love Python')
myFile.write('and I am feeling good doing this refresh')
myFile.close()

# Append to file
myFile = open('myfile.txt', 'a') # 'a' to append if we did 'w' it would overwrite what is in there already
myFile.write('\nI am also feeling a little overwhelmed cause there is a lot to review!')
myFile.close()

# Read from a file
myFile = open('myfile.txt', 'r+')
text =myFile.read(100)
print(text)