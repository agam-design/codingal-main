file=open('fileHandling.txt')
print(file.read())
file.close()


file=open('fileHandling.txt','r')
print('read in parts.')
print(file.read(5))
file.close()

file=open('fileHandling.txt')
file2=open('fileHandling2.txt','w')

for line in file.readlines():
    if not(line.startswith('Agam')):
        print(line)
        file2.write(line)

file.close()
file2.close()

