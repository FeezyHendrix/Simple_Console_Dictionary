import json
from difflib import get_close_matches as match

data = json.load(open("Data.json"))


def searchDict(keyword):
    keyword = keyword.lower()
    if keyword in data:
        i = 1
        for df in data[keyword]:
            print(str(i) + '. ' + df)
            i = i + 1

    elif len(match(keyword, data.keys())) > 0:
        reply = input("Did you mean %s instead ? Y/N " % match(keyword, data.keys())[0])
        reply = reply.lower()
        if reply == 'y':
            i = 1
            for df in data[match(keyword, data.keys())[0]]:
                print(str(i) + '. ' + df)
                i = i + 1

        else:
            print("Sorry we don't know the word you are looking for")

    elif keyword == 'q':
        quit()
    else:
        return print("The word does'nt exist, kindly double check your spellings")


def Dictionaryopen():
    while True:
        keyword = input("(Hint to Quit Enter 'q') Enter Word : ")
        searchDict(keyword)



Dictionaryopen()
