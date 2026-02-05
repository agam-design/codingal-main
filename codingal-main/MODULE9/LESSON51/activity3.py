# Write a Python program to duplicate from one file and then copy it to another file. For copying it in a new file, create a new empty file and upload it in a similar way as you do for the given file.
outputFile=open('updatedFile.txt','w')
inputFile=open('repeatedFile.txt','r')

linesSeenSoFar=set()
print("eliminating duplicate lines.")

for line in inputFile:
    if line not in linesSeenSoFar:
        outputFile.write(line)
        linesSeenSoFar.add(line)#adds unique lines to linesSeenSofar.

outputFile.close()
inputFile.close()



