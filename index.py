from sys import argv
from pprint import pprint

fileName = argv[1]
text = open(fileName, "r").read()


#metindeki kelimelerin oldugu indexleri listeler halinde dictionaride saklar
def indexation(text):
    d = {}
    index = 0
    indexList = []
    word = ""
    for c in text.lower():
        if not c.isalnum():
            if not word == "":
                m = d.get(word, [])
                m.append(index-len(word))
                indexList.append(index-len(word))
                d[word] = m
            word = ""
        else:
            word = word + c
        index += 1
    return d, indexList


"""indexlenmis kelime listesini ve indexleri alir,
aranan kelimenin her bir indexini,
kendisinin onundeki ve sonundaki kelimelerle beraber bir listeye ekler.
ve bu listelerin oldugu bir liste doner"""


def search(word, indexData):
    d, indexList = indexation(indexData)
    listem = []
    """ if not word in d gibi kullanirsan not word olarak algilar."""
    if word not in d:
        return "there is no such word!"
    for i in d[word]:
        ind = indexList.index(i)
         # kelime obeginin bulundugu soz obegi
        l = [str(i), word]
        """kelimenin bulundugu indexin once ve sonrasinda kelime varsa
        bunu soz obegine ekle"""
        for x in d:
            if indexList[ind - 1] in d[x] and ind != 0:
                l.insert(1, x)
            if ind < len(indexList) - 1 and indexList[ind + 1] in d[x]:
                l.append(x)
        listem.append(" ".join(l))
    return listem


if __name__ == "__main__":
    while 1:
        word = raw_input("what word you are seacrhing for: ")
        pprint(search(word, text))
