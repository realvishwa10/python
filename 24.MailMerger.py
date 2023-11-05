# Mail merger
PLACEHOLDER = "[name]"

with open("C:\\Users\\Vishwa\\Downloads\\Mail+Merge+Project+Start\\Mail Merge Project Start\\Input\\Names\\invited_names.txt") as names_file:
    names = names_file.readlines()

with open("C:\\Users\\Vishwa\\Downloads\\Mail+Merge+Project+Start\\Mail Merge Project Start\\Input\\Letters\\starting_letter.txt", mode='r') as letter_file:
    letter_content = letter_file.read()

    for name in names:
        stripped_name = name.strip()
        replaced_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        new_letter = replaced_letter
        with open(f"C:\\Users\\Vishwa\\Downloads\\Mail+Merge+Project+Start\\Mail Merge Project Start\\Output\\ReadyToSend\\invite_for_{stripped_name}.txt", mode='w') as new_file:
            new_file.write(new_letter)

    # for name in file2:
    #     new_file = file1.replace
# with open("C:\\Users\\Vishwa\\Downloads\\Mail+Merge+Project+Start\\Mail Merge Project Start\\Input\\Names\\invited_names.txt", mode='w') as file:
