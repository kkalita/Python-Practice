import json

def translate(word):

    word = word.lower()
    
    if word in words:
        return words[word]
    else: 
        return "The word doesn't exist - double check it"

words = json.load(open("data.json"))
userreq = input("Enter word to get definition: ")

print(translate(userreq))

