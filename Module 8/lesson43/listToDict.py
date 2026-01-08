# Write a program to create a List with five students' details (roll no, name, grade). Then convert that list into a dictionary.
students=[[2,"Riya",6],[3,"Zara",7],[5,"Agam",10],[7,"zoe",7],[9,"rahul",9]]# this is an example of list of list
def convert(x):
    result={}
    for i in x:
        result[i[0]]=i[1:]
    return(result)

print('orginal list is ', students)
print("converted list to dictionary ", convert(students))


















