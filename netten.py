# -*- coding: utf-8 -*-

birler = ["", "bir ","iki ",u"üç ",u"dört ", u"beş ", u"altı ", "yedi ","sekiz ", "dokuz "]
onlar = ["","on ","yirmi ","otuz ",u"kırk ", "elli ",u"altmış ",u"yetmiş ","seksen ","doksan "]
binler = ["","bin ","milyon ", "milyar ", "trilyon ", "katrilyon "]

def numberText(n):
    n3 = []
    r1 = ""
    ns = str(n)
    for k in range(3, 33, 3):
        r = ns[-k:]
        q = len(ns) - k
        if q < -2:
            break
        else:
            if  q >= 0:
                n3.append(int(r[:3]))
            elif q >= -1:
                n3.append(int(r[:2]))
            elif q >= -2:
                n3.append(int(r[:1]))
        r1 = r

    nw = ""
    for i, x in enumerate(n3):
        b1 = x % 10
        b2 = (x % 100)//10
        b3 = (x % 1000)//100
        if x == 0:
            continue
        else:
            t = binler[i]
        if b2 == 0:
            nw = birler[b1] + t + nw
        elif b2 == 1:
            nw = onlar[1] + birler[b1] + t + nw
        elif b2 > 1:
            nw = onlar[b2] + birler[b1] + t + nw
        if b3 > 0:
            nw = birler[b3] + u"yüz " + nw
    return nw.strip()

print numberText("100")
