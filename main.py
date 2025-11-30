def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    #print(file_contents)
    return file_contents

def word_count(input_file_contetns):
    words = input_file_contetns.split()
    print(len(words))

def character_count(input_string):

    character_set = set(input_string)
    unique_characters = set()
    for character in character_set:
        unique_characters.add(character.lower(): 1)
    print(unique_characters)
file_contents = main()
word_count(file_contents)
new_variable = character_count(file_contents)

#print(new_variable)
