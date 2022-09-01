import pandas as pd

nato_alphabet = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (key, row) in nato_alphabet.iterrows()}

user_input = input("Please enter a name: ").upper()
result = [nato_dict[key] for key in user_input]

