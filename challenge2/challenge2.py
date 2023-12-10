#height
height=float(input("Enter your height in meters :\n"))
#weight
weight=float(input("Enter your weight in Kgs: \n"))
#BMI
BMI=round(weight/(height**2),2)
print("The BMI of the person is : "+str(BMI)+"\n")