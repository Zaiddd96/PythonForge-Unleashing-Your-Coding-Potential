#Password Generator
import random
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["1","2","3","4","5","6","7","8","9","10"]
characters = ["!","@","#","$","%","^","&","*","(",")"]
print("Welcome to the password generator!")
hm_letters = int(input("How many letters do you want in your password: "))
hm_numbers = int(input("How many numbers in your password: "))
hm_chars = int(input("How many special characters you want in your password: "))

password = []
for alpha in range(1,hm_letters+1):
    password.append(random.choice(letters))

for num in range(1,hm_numbers+1):
    password.append(random.choice(numbers))

for char in range(1,hm_chars+1):
    password.append(random.choice(characters))

random.shuffle(password)
hard = ""
for pwd in password:
    hard += pwd

print(f"Your password is : {hard}")
