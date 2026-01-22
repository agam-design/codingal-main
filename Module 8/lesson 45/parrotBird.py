#Write a program to create a class Parrot and perform the following tasks - Create a class variable species Create a __init__ method that has instance variables - name and age Create instances of class Parrot, passing arguments as well Print Class variable by accessing it Print Instance variables as well
class parrot:
    species="bird"

    def __init__(self,name,age):
        self.name=name
        self.age=age

ob1=parrot("blue",3)#instance of the class parrot
ob2=parrot("koo",5)

print("blue is a ", ob1.species)
print("koo is a ", ob2.species)

print(ob1.name,"is ",ob1.age,"years old")
print(ob2.name,"is ",ob2.age,"years old")



