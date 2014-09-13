d = {"cemil": "can", "canan": "duran", "betul": "sibel", "sahin": "metin"}


def where(x, dic):
    return [i for i in dic if x in i]

print where("a", d)
