import json

data = json.load(open("data.json"))
word = input("please enter some words to search in dictionary:")
result = data[word]
print(result)
