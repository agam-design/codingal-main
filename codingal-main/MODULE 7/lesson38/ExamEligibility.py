age = int(input("Enter your age: "))
citizenship = input("Enter your country: ")

if age >= 18:
    if citizenship.lower() == "india": 
        print("You are eligible for NEET exam.")
    else:
        print("You are not eligible for NEET exam.")
else:
    print("You are not eligible for NEET exam.")
