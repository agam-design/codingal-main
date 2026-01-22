#Write a program to create a parent class Person (attributes - fname, lname) with a method printname to display the full name. Create a child class Student (attributes - fname, lname, year). Access the attributes of parent class in child class using super() function. Then, create an object for the child class and call the display method to display the full name. Also, print the graduation year.
class person(object):
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def printName(self):
        print(self.fname,self.lname)

class student(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.year=year
ob=student("agam","pawar",2008)
ob.printName()
print(ob.year)