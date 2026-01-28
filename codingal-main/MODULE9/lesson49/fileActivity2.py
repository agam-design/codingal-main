file=open('codingal-main/MODULE9/lesson49/file.txt')#open file and store the file object in a variable.
print(file.read())# read the content of the file.
file.close()# close the file

fileWrite=open('codingal-main/MODULE9/lesson49/file.txt','w')
fileWrite.write("i love coding")
fileWrite.write("I'm gagan")
fileWrite.close()

fileAppend=open('codingal-main/MODULE9/lesson49/file.txt','a')
fileAppend.write("file in append mode")
fileAppend.write("\ni love dancing.")
fileAppend.close()