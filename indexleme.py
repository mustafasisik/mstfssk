from sys import argv
from pprint import pprint
myFileName = argv[1]
f = open(myFileName, "r")
text = f.read()


def listele(text):
    listem = []
    index = 0
    word = ""
    for c in text.lower():
        if not c.isalnum():
            if not word == "":
                listem.append(str(index-len(word)))
                listem.append(word)
            word = ""
        else:
            word = word + c
        index += 1
    return listem


def search(text, word):
    l = listele(text)
    result = []
    while word in l:
        sentence = []
        x = l.index(word)
        sentence.append(l[x-1])
        sentence.append(l[x-2])
        sentence.append(l[x])
        sentence.append(l[x+2])
        result.append(sentence)
        l = l[x+1:]
    return result


if __name__ == "__main__":
    while 1:
        word = raw_input("what word you are seacrhing for: ")
        pprint(search(text, word))
