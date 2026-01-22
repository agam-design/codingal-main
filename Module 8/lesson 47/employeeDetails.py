#Write a program to create a parent class Person (attributes - name, idnumber) with a method display to display the attributes. Create a child class Employee (attributes - name, idnumber, salary, post). Access the attributes of parent class in child class. Then, create an object for child class and call the display method to display the name and idnumber.
class  parent(object):
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)

class employee(parent):
    def __init__(self,name,idnumber,salary,post):
        self.salary=salary
        self.post=post
        parent.__init__(self,name,idnumber)

ob=employee("agam", 5746, 5000,"junior")
ob.display()