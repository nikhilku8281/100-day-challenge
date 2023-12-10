#welcome message
print("Welcome to the tip calculator :")
#bill for the food
bill=float(input("\nWhat is the total bill : "))
#tip on the bill
tip=float(input("\nWhat percentage of the tip would you like to give? "))
#no of guests
guests=int(input("\nHow many people to split the bill ? :"))
#calculate each people share
total_bill=bill+bill*tip/100
each_person_share=round(total_bill/guests,2)
each_person_share="{:.2f}".format(each_person_share)
print(f"\n Each person should pay : ${each_person_share}")