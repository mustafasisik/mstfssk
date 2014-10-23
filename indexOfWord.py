from sys import argv
script, fileName, word = argv

def indexation(textName):
    d = {}
    sentenceList = textName.split(".")
    wordNumber = 0
    for sentence in sentenceList:
        sentenceIndex = []
        for word in sentence.split():
            sentenceIndex.append(wordNumber)
            if not word in d:
                d[word] = [(wordNumber, sentenceIndex)]
            else:
                d[word].append((wordNumber, sentenceIndex))
            wordNumber += 1
    return d


print indexation(text)
