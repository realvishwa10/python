# Ceaser's cypher

alphabets = "abcdefghijklmnopqrstuvwxyz"
alpha_list = list(alphabets)

# Making the list twice long so words with z can also find shift in position
alphabet_list = alpha_list + alpha_list
loop = True

while loop:
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n").lower()
    text = input("Enter your message:\n").lower()
    shift = int(input("Type your shift number:\n"))
    shift = shift % 26

    def encrypt(start_text, shift_amount, shift_direction):
        word = ""
        if shift_direction == "decode":
            shift_amount *= -1
        for letter in start_text:
            if letter in alphabet_list:
                position = alphabet_list.index(letter)
                new_position = position + shift_amount
                new_letter = alphabet_list[new_position]
                word += new_letter
            else:
                word += letter
        print(f"Your {shift_direction}d word is: {word}")

    encrypt(start_text=text, shift_amount=shift, shift_direction=direction)
    alter_loop = input("Type 'yes' to continue and 'no' to end:\n").lower()
    if alter_loop == "no":
        loop = False

print("Goodbye")