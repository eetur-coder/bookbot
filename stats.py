def word_count(input_file_contetns):
    words = input_file_contetns.split()
    return len(words)
'''
def character_count(input_string):
    character_set = set(input_string)
    unique_characters = set()
    for character in character_set:
        unique_characters.add(character.lower())
    return(unique_characters)
'''
def character_count(input_string):
    character_dict = {} #loin uuden tyhjän dictionaryn
    for character in input_string: #looppasin kirjan sisällön eli kirjaimen kerrallaan
        lower_char = character.lower() #muutin kirjaimen pieneksi
        if lower_char in character_dict: #tarkistin onko pieni kirjain jo dictionaryssä ja jos on niin...
            character_dict[lower_char] = character_dict.get(lower_char, 0) + 1 # kasvatin yhdellä nyt loopissa olevan kirjaimen dictionary key:hin
        else:
            character_dict[lower_char] = 1 #tai jos key:tä ei vielä ollut eli tuli uusi kirjain vastaan niin muutin sen 1
    return(character_dict) #palautin tuon dictionaryn Mainiin.
    #return sort_dictionary(character_dict)

def sort_dictionary(items):
    newList = []
    for key, value in items.items():
        if key.isalpha():
            newList.append({"char": key, "num": value})

    def sort_on(item):
        return item["num"]
    
    newList.sort(reverse=True, key=sort_on)
    return newList
    #print(characters)
    #return character_dict
