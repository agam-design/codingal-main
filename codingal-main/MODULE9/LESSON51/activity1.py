#write a file using with() and split file into words.
with open('outsideFile3.txt','r')as file:
    data=file.readlines()
    print("words in the file are ")
    for line in data:
        word=line.split()
        print(word)

file.close()


    

