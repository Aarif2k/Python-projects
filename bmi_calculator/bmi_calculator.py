Height = float(input("Enter your height in centimetre:"))
Weight = float(input("Enter your weight in kilogram:"))
Height = Height/100
BMI = Weight / (Height*Height)
print("Your BMI is",BMI)
if BMI>0:
    if BMI<=16:
        print("You are severely underweight")
    elif BMI<=18.5:
        print("You are underweight")
    elif BMI<=25:
        print("You are healthy")
    elif BMI<=18.5:
        print("You are overweight")
    else:
        print("You are severely overweight") 
else:
    print("Please enter valid details.")   