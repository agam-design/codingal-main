myTuple=()#empty Tuple
myTuple=(1,2)
myTuple=(4,5.7,"hi")
myTuple=((4,5,6),(7,8,9),10)#nested tuples
myTuple=("a","b","c")
print(myTuple[0])
myTuple1=((4,5,6),(7,8,9),10)#nested tuples
print(myTuple1[0][1])
print("sliced",myTuple[0:2])
for letter in (myTuple):
    print("hello", letter)



