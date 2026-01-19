#Write a program to create a class Parrot and perform the following tasks - Create a class variable species Create a __init__ method that has instance variables - name and age Create instances of class Parrot, passing arguments as well Print Class variable by accessing it Print Instance variables as well
class parrot:
    species="bird"

    def __init__(self,name,age):
        self.name=name
        self.age=age

ob1=parrot("parrot1",3)#instance of the class parrot
ob2=parrot("parrot2",5)

print("Parrot is a ", parrot.species)
print(ob1)


