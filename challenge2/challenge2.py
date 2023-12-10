#height
height=float(input("Enter your height in meters :\n"))
#weight
weight=float(input("Enter your weight in Kgs: \n"))
#BMI
BMI=round(weight/(height**2),2)
if BMI < 18.5:
    print(f"The BMI of the person is : {BMI}, you are Underweight \n")
elif BMI < 25:
    print(f"The BMI of the person is : {BMI}, you are Normal \n")
elif BMI< 30:
    print(f"The BMI of the person is : {BMI}, you are slightly Overweight \n")
elif BMI<35:
    print(f"The BMI of the person is : {BMI}, you are Obese \n")
else:
    print(f"The BMI of the person is : {BMI}, you are clinically Obese \n")


