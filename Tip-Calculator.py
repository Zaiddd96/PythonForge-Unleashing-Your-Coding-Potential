
#Tip calculator!
print("Welcome to the tip calculator!")
bill = float(input("Enter your Bill: $"))
tip = int(input("How much tip you want to give? %"))
tip_plus_bill = bill + (bill * tip / 100 )
split = int(input("Among how many person you want to split?"))
Split = tip_plus_bill / split
print(f"Each person has to pay: {round(Split,2)} ")