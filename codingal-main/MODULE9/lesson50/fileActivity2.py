file=open('outsideFile.txt')
print(file.read())
file.close()

fileWrite=open('outsideFile.py','w')
fileWrite.write("hi! I'm Agam")
fileWrite.close()

fileAppend=open('outsideFile.py','a')
fileAppend.write("I'm 17 years old")
fileAppend.close()

