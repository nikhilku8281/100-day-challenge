#input the year
leap_year=int(input("Enter the year: "))
print("\n")
if leap_year % 4 == 0:
    if leap_year % 100 == 0:
        if leap_year % 400 == 0:
            print("\n Leap Year")
        else:
            print("\n Not a leap year")
    else:
        print("\n leap year")
else:
    print("\n Not a leap Year")

