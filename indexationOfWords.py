from sys import argv
fileName = argv[1]
word = argv[2]
fileText = open(fileName, "r").read()


def indexation(text, word):
    d = {}
    sentenceList = text.split(".")
    index = 0
    for sentence in sentenceList:
        wordBefore1 = ""
        wordBefore2 = ""
        for w in sentence.split():
            if not wordBefore1 in d:
                d[wordBefore1] = [(index-1, wordBefore2, wordBefore1, w)]
            else:
                d[wordBefore1].append((index-1, wordBefore2, wordBefore1, w))
            index += 1
            wordBefore2 = wordBefore1
            wordBefore1 = w

    return d[word]


assert indexation(fileText, word) == [(9, "that", "she", "sells"), (17, "if", "she", "sells")]
print indexation(fileText, word)
