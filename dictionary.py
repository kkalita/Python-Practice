import json


def translate(word):
    return words[word]




words = json.load(open("data.json"))
userreq = input("Enter word to get definition: ")

print(translate(userreq))