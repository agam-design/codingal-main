#Write a program to create a class with the name employee and create a constructor and destructor. Then, create an object for that class and delete the object.
class employee:
    def __init__(self):
        print("employee created")
    def __del__(self):
        print("destructor called, employee deleted")
ob=employee()
del ob

