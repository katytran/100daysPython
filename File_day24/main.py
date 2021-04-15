# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt

# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = []
with open("./Input/Names/invited_names.txt") as data:
    name_content = data.readlines()
    for name in name_content:
        with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
            letter_content = letter.read().replace("[name]", name.strip())
            print(letter_content)
            path = f"./Output/ReadyToSend/{name}"
            print(path)
            with open(path, mode="w") as newletter:
                newletter.writelines(letter_content)









