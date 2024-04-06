
#Tip calculator!
print("🎩 Welcome to the Tip Calculator! 🎩")
bill = float(input("Enter your bill amount: $"))
tip_percentage = int(input("How much tip would you like to give? (Enter a percentage): "))
total_amount = bill * (1 + tip_percentage / 100)
num_people = int(input("How many people are splitting the bill? "))
amount_per_person = total_amount / num_people
print(f"Each person should pay approximately: ${round(amount_per_person, 2)}")
