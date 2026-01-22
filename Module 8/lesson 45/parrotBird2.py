class parrot():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sing(self,song):
        # return self.name,"sings ", song
        return "{} sings {}".format(self.name,song)
    def dance(self):
        # return self.name, "is dancing "
        return "{} is dancing".format(self.name)
ob=parrot("koo",5)
print(ob.sing("happy"))
print(ob.dance())
