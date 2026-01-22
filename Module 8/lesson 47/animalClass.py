#Write a program to implement abstraction on animal class (base class). The abstract method will be move that is for displaying what subclasses can do.
from abc import ABC, abstractmethod
class animal(ABC):
    def move(self):
        pass
class dog(animal):
    def move(self):
        print("I can bark")
class lion(animal):
    def move(self):
        print("I can roar")
class bird(animal):
    def move(self):
        print("I can fly")  
ob1=dog()
ob1.move()
ob2=lion()
ob2.move()
ob3=bird()
ob3.move()