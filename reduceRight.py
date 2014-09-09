def combineText(x, y):
    return x + y

l = ["hasan ", "eve ", "git ", "gec ", "kalma"]


def reduceRigth(f, liste):
    while len(liste) > 1:
        liste[len(liste) - 2] = f(liste[len(liste) - 2], liste[len(liste) - 1])
        liste = liste[:-1]
        print liste
    print liste[0]


reduceRigth(combineText, l)

assert combineText("ahmet", "cemil") == "ahmetcemil"
