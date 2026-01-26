#Write a program to create a class Computer with a private attribute max_price and methods sell(to display) the selling price and setmaxprice(change the private attribute max_price). Now create an object for the class Computer. Try changing the value of max price and use the sell function to display the updated price. Use a setter function to update the value and again display the price.
class computer:
    def __init__(self):
        self.__maxPrice=900 #__maxPrice is the private attribute.
    def sell(self):
        print(f"selling price: {self.__maxPrice}.")
    def setMaxPrice(self,price): #setter function to update the private attribute.
        self.__maxPrice=price
ob1=computer()
ob1.sell()

ob1.__maxPrice=1000 # trying to change the maxPrice directly.It will not change.
ob1.sell()

ob1.setMaxPrice(1000) # trying to change the maxPrice using setter function.Modifications are possible, it will change.
ob1.sell()
