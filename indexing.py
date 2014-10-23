from sys import argv
fileName = argv[1]
word = argv[2]
text = open(fileName, "r").read()


def indexing(text, word):
    d = {}
    index = 0
    for w in text.split():
        if word == w.strip(",") or word == w.strip(";") or word.lower() == w.lower():
            if not word in d:
                d[word] = [(index, text[index-8: index + 13])]
            else:
                d[word].append((index, text[index-8: index + 13]))
        index += len(w) + 1
    return d


print indexing(text, word)
