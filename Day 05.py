# PASSWORD GENERATOR

import random

alphabets = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
organized_alphabets = alphabets.split(" ")

numbers = "0 1 2 3 4 5 6 7 8 9"
organized_numbers = numbers.split(" ")

symbols = "! # $ % & ( ) * +"
organized_symbols = symbols.split(" ")

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))

word = ""
for letter in range(0, nr_letters):
    random_letter = random.randint(0, len(organized_alphabets)-1)
    word += organized_alphabets[random_letter]

digit = ""
for number in range(0, nr_numbers):
    random_number = random.randint(0, len(organized_numbers)-1)
    digit += organized_numbers[random_number]

sign = ""
for symbol in range(0, nr_symbols):
    random_symbol = random.randint(0, len(organized_symbols)-1)
    sign += organized_symbols[random_symbol]

new_pass = f"{word}{digit}{sign}"
# random_pass = ""
# for length in range(1, len(new_pass)):
#     pick = random.randint(0, len(new_pass))
#     random_pass += new_pass[pick]

random_pass = ''.join(random.sample(new_pass, len(new_pass)))
print(f"Your Password is : {word}{digit}{sign}")

