file=open('codingal-main/MODULE9/lesson49/file.txt')
counter=0

content=file.read()
contentList=content.split("\n") #splitting the content into lines and storing them in a list.

for i in contentList:
    if i:
        counter += 1 #it means counter= counter + 1

print("total number of lines are ", counter)