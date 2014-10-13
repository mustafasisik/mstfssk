text = """bugun hava cok guzel. bu yuzden bugun disari cikip hava almak istiyorum.
cok yorgunum ama bir daha bu havayi bulacagimi sanmiyorum."""

def indexOfWords(textName):
    d = {}
    wordList = textName.split()
    for word in wordList:
        indexList = []
        index = 0
        for w in wordList:
            index += 1
            if w == word:
                indexList.append(index)
        d[word] = indexList
    return d



print indexOfWords(text)
