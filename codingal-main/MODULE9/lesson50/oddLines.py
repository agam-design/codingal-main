file=open('outsideFile.txt')
file2=open('outsideFile2.txt','w')

content=file.readlines()
type(content)
for i in range(1,len(content)+1):
    if(i%2 !=0):
        file2.write(content[i-1])
    else:
        pass
file2.close()
file2=open('outsideFile2.txt','r')

content2=file2.read()
print(content2)
file.close()
file2.close()