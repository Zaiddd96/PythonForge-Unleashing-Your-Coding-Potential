import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

dick = {name.letter: name.code for idx, name in data.iterrows()}

user = input("Enter your name: ").upper()
nato_phonetic = [dick[letter] for letter in user]
print(nato_phonetic)