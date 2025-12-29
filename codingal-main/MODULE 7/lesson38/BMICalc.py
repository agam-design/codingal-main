height = float(input("enter the height in cm "))
weight = float(input("enter the weight in kg "))

BMI = weight/(height/100)**2

if BMI<=18.4: 
    print("you are underweight. ")
elif BMI<=24.9:
    print("you are healthy. ")
elif BMI<=29.9:
    print("you are overweight. ")
elif BMI<=34.9:
    print("you are severely overweight. ")
elif BMI<=39.9:
    print("you are Obese. ")
else :
    print("you are severly Obese. ")