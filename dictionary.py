import json
from difflib import get_close_matches

words = json.load(open("data.json"))

def translate(word):

    word = word.lower()
    
    if word in words:
        return words[word]
    elif get_close_matches(word, words.keys()):
        yn = input("Did you mean %s? Enter Y/N: " % get_close_matches(word, words.keys())[0])

        if yn.lower() == "y":
            return words[get_close_matches(word, words.keys())[0]]

    else: 
        return "The word doesn't exist - double check it"

def main():
    userreq = input("Enter word to get definition: ")

    print(translate(userreq))

if __name__ == "__main__":
    main()