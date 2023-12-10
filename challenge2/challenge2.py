#height
height=float(input("Enter your height in meters :\n"))
#weight
weight=float(input("Enter your weight in Kgs: \n"))
#BMI
BMI=round(weight/(height**2),2)
print(f"The BMI of the person is : {BMI} \n")