# Write a Python program to merge the contents of two different files into a third file. Create this new third file first and then copy the contents.
with open('outsideFile3.txt')as file1:
    data1=file1.read()
with open('outsideFile2.txt')as file2:
    data2=file2.read()

data1+="\n"
data1+=data2
print("emerging 2 files.")

with open('emergedFile.txt','w')as file3:
    file3.write(data1)



