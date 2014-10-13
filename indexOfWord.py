text = """bugun hava cok guzel. bu yuzden bugun disari cikip hava almak istiyorum.
cok yorgunum ama bir daha bu havayi bulacagimi sanmiyorum."""

def indexOfWords(textName):
    d = {}
    sentenceList = textName.split(".")
    sentenceNumber = 0
    for sentence in sentenceList:
        sentenceNumber += 1
        wordNumber = 0
        for word in sentence.split():
            wordNumber += 1
            if not word in d:
                d[word] = [(sentenceNumber, wordNumber)]
    return d




print indexOfWords(text)
