with open('outsideFile2.txt','r')as file:
    data=file.readlines()
    print("words in the file are ")
    for line in data:
        word=line.split()
        print(word)

file.close()

outputFile=open('updatedFile.txt','w')
inputFile=open('repeatedFile.txt','r')

linesSeenSoFar=set()
print("eliminating duplicate lines.")

for line in inputFile:
    if line not in linesSeenSoFar:
        outputFile.write(line)
        linesSeenSoFar.add(line)

outputFile.close()
inputFile.close()

with open('outsideFile2.txt')as file1:
    data1=file1.read()
with open('fileHandling2.txt')as file2:
    data2=file2.read()

data1+="\n"
data1+=data2
print("emerging 2 files.")

with open('emergedFile2.txt','w')as file3:
    file3.write(data1)





