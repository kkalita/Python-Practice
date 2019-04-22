import json
from difflib import get_close_matches

words = json.load(open("data.json"))

#lowercase dictionary

def translate(word):

    word = word.lower()
    
    if word in words:
        return words[word]
    elif get_close_matches(word, words.keys()):
        closest = get_close_matches(word, words.keys())[0]
        yn = input("Did you mean %s? Enter Y/N: " % closest)

        if yn.lower() == "y":
            return words[closest]
        else:
            return "The word doesn't exist"

    else: 
        return "The word doesn't exist"

def main():
    userreq = input("Enter word to get definition: ")
    definition = translate(userreq)

    if type(definition) == list:
        for i in definition:
            print(i)
    else:
        print(definition)

    input()

if __name__ == "__main__":
    main()