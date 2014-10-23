from sys import argv
from pprint import pprint

fileName = argv[1]
word = argv[2]
text = open(fileName, "r").read()


def indexation(text, w):
    d = {}
    result = {}
    index = 0
    indexList = [0]
    word = ""
    for c in text.lower():
        if not c.isalnum():
            if not word == "":
                indexList.append(index+1)
                m = d.get(word, [])
                m.append(index-len(word))
                d[word] = m
            word = ""
        else:
            word = word + c
        index += 1
    for x in d[w]:
        if x == indexList[0]:
            result[x] = text[: indexList[indexList.index(x) + 2]]
        elif x == indexList[len(indexList)-1]:
            result[x] = text[indexList[indexList.index(x)-1]:]
        else:
            result[x] = text[indexList[indexList.index(x)-1]: indexList[indexList.index(x) + 2]]
    return result

pprint(indexation(text, word))
