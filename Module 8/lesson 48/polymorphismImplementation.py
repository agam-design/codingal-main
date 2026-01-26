#Write a program to create two classes Dog and Cat, with the same attributes - (name and age) and methods - (info and make_sound). Create different objects for each class and pass the parameters. Showcase the concept of polymorphism in this program.
class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"I'm a dog.My name is {self.name}.I'm {self.age} years old.")
    def make_sound(self):
        print("bark")

class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"I'm a cat. My name is {self.name}. I'm {self.age} years old.")
    def make_sound(self):
        print("meow")

ob1=dog("tommy",3)
ob2=cat("rio",4)

for animal in (ob1,ob2):
    animal.info()
    animal.make_sound()

        