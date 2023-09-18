# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = float(weight/height**2)

BMI = round(BMI)
Value = (f"Your BMI is {BMI}")
#print(Value)

if BMI<=18.5:
    print(f"{Value}, you are underweight.")
elif 18.5<BMI<=25:
    print(f"{Value}, you have a normal weight.")
elif 25<BMI<=30:
    print(f"{Value}, you are slightly overweight.")
elif 30<BMI<=35:
    print(f"{Value}, you are obese.")
else:
    print(f"{Value}, you are clinically obese.")
