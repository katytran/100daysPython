student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}


#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
with open("nato_phonetic_alphabet.csv") as data:
    content= data.readlines()

dictionaries = {code.strip()[0]:code.strip()[2:] for code in content[1:]}

file = pandas.read_csv("nato_phonetic_alphabet.csv")

# for (index, row) in file.iterrows():
#     print(row.letter)
#     #Access index and row
#     #Access row.student or row.score

dictionaries2 = {row.letter: row.code for (index, row) in file.iterrows()}
print(dictionaries2)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_name():
    name = input("Input your name: ").upper()
    try:
        code_name = [dictionaries[letter] for letter in name]
    except:
        print("Letter only")
        generate_name()
    else:
        print(code_name)


generate_name()









