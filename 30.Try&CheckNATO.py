# Refining NATO-code generator through exception handling
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

"""SOLVING THROUGH WHILE LOOP"""
# correct_input = True
# while correct_input:
#     try:
#         word = input("Enter a word: ").upper()
#         phonetic_code = [data_dict[letter] for letter in word]
#     except KeyError:
#         print("Sorry. Only letters in the alphabet please")
#     else:
#         print(phonetic_code)
#         correct_input = False

"""SOLVING THROUGH FUNCTION DEFINING"""


def generate_code():
    word = input("Enter a word: ").upper()
    try:
        phonetic_code = [data_dict[letter] for letter in word]
    except KeyError:
        print("Sorry. Only letters in the alphabet please")
        generate_code()
    else:
        print(phonetic_code)


generate_code()
