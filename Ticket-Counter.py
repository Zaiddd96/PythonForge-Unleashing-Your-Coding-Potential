#Roller coaster ticket counter!
print("Welcome o the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height < 120:
    print("Sorry! you cant ride the rollercoaster!")
else:
    print("Yes, you can ride the rollercoaster!")
    age = int(input("Enter your age: "))
    if age < 12:
        bill = 5
        print("Your ticket price is $5.")
    elif age <= 18:
        bill = 7
        print("Your ticket is $7.")
    elif age >= 45 and age <= 55:
       print("You don't have to pay the ticket!")
    else:
        bill = 12
        print("Your ticket price is $12.")
    photo = input("Do you wan't a photo? Y or N: ")
    if photo == 'y':
        bill += 3

    print(f"your total bill is ${bill}")
    