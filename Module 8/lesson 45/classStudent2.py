#Write a program to create a class with name Student and perform the following tasks - Create a class variable grade and name Create a function to print a sentence Create a function to print class variables grade and name Create an object of class Student Call the two functions to execute them
class student:
    Grade=8
    name="Riya"

    def introduction(self):
        print("Hi! I'm a student")
    
    def mySelf(self):
        print("My name is ", self.name)
        print("I study in grade ", self.Grade)

ob=student()
ob.introduction()
ob.mySelf()






























