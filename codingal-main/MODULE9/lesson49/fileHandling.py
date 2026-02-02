file=open('outsideFile.py')
print(file.read())
file.close()

fileWrite=open('outsideFile.py','w')
fileWrite.write("I'm NEET aspirant.")
fileWrite.write("I don't like PHYSICS.")
fileWrite.close()

fileAppend=open('outsideFile.py','a')
fileAppend.write("\nThe NEET exam will take place in 2027.")
fileAppend.write("\nI love BIOLOGY.")
fileAppend.close()

