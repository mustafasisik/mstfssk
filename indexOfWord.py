text = """bugun hava cok guzel. bu yuzden bugun disari cikip hava almak istiyorum.
cok yorgunum ama bir daha bu havayi bulacagimi sanmiyorum."""

def indexOfWord(textName):
    d = {}
    sentenceList = textName.split(".")
    wordNumber = -1
    for sentence in sentenceList:
        sentenceIndex = []
        for word in sentence.split():
            wordNumber += 1
            sentenceIndex.append(wordNumber)
            if not word in d:
                d[word] = (wordNumber, sentenceIndex)
    return d


print indexOfWord(text)
