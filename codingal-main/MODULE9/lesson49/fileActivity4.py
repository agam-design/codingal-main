#Write a Python program that can append the content of one file to another file.
firstFile=input("enter file 1.")
secondFile=input("enter file 2.")


f1=open(firstFile,'r')
f2=open(secondFile,'r')

print('content of first file before appending \n',f1.read())
print('content of second file before appending \n',f2.read())

f1.close()
f2.close()

#opening first file in append mode and second file in read mode
f1=open(firstFile,'a+')
f2=open(secondFile,'r')

f1.write(f2.read()) #appending context of second file to the first file.

f1.seek(0) #relocating the cursor of the files at the beginning.
f2.seek(0)

print('content of first file after appending \n',f1.read())
print('content of second file after appending \n',f2.read())

f1.close()
f2.close()

