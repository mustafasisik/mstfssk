def find(liste, word):
    for w in liste:
        if w == word:
            return liste.index(w), w


print find(["ahmet", "cemil", "dursun", "sahan"], "dursun")

