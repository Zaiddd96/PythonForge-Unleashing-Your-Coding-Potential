#Python Pizza Delivery System!
print("🍕 Welcome to Python's Pizzeria, where every slice is a byte of delight! 🍕")
size = input("Choose the size of your adventure: Small (S), Medium (M), or Large (L)? ")
add_pepperoni = input("Fancy some pepperoni on top? Yes (Y) or No (N)? ")
extra_cheese = input("How about an extra layer of cheesy goodness? Yes (Y) or No (N)? ")

bill = 0
if size == "S":
  bill = 15
  if add_pepperoni == "Y":
    bill += 2
  if extra_cheese == "Y":
    bill += 1
elif size == "M":
  bill = 20
  if add_pepperoni == "Y":
    bill += 3
  if extra_cheese == "Y":
    bill += 1
else:
  bill = 25
  if add_pepperoni == "Y":
    bill += 3
  if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
