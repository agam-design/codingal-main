file1=open('outsideFile.txt')
file2=open('outsideFile2.txt','w')

for line in file1.readlines():
    if not (line.startswith('coding')):
        print(line)
        file2.write(line)

file1.close()
file2.close()