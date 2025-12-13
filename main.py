import sys
from stats import character_count, sort_dictionary, word_count

def get_book_text(path):
        with open(path) as f:
            return f.read()
    #print(file_contents)
def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    charCount = character_count(text)
    characterDict = sort_dictionary(charCount)
    wordCount = word_count(text)
    print(f"Found {wordCount} total words")
    for dictItem in characterDict:
        print(f"{dictItem['char']}: {dictItem['num']}")
    
    #print(f"Found {word_count(text)} total words")

#word count in stats.py


#file_contents = main()
#filePath = "books/frankenstein.txt"
main()
#word_count(file_contents)
#new_variable = character_count(file_contents)
#print(new_variable)
#print("greetings boots")