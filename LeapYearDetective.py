#leapyear Detecive!
year = int(input("Enter the year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"The year {year} is a leap year!")
        else:
            print("This is not a leap year.")
    else:
        print(f"The year {year} is a leap year!")
else:
    print("This is not a leap year.")