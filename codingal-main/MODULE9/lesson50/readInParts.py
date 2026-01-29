file=open('outsideFile.txt')
print(file.read())
file.close()

file=open('outsideFile.txt', 'r')
print('read in parts')
print(file.read(8)) #read the beginning 8 characters.
file.close()