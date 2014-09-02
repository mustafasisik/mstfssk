# coding: utf-8
d_birler = {"0": "",
 "1": "Bir",
 "2": "Iki",
 "3": "Uc",
 "4": "Dort",
 "5": "Bes",
 "6": "Alti",
 "7": "Yedi",
 "8": "Sekiz",
 "9": "Dokuz"}

d_onlar = {"0": "",
 "1": "On",
 "2": "Yirmi",
 "3": "Otuz",
 "4": "Kirk",
 "5": "Elli",
 "6": "Altmis",
 "7": "Yetmis",
 "8": "Seksen",
 "9": "Doksan"}

d_yuzler = {"0": "",
 "1": "Yuz",
 "2": "IkiYuz",
 "3": "UcYuz",
 "4": "DortYuz",
 "5": "BesYuz",
 "6": "AltYuz",
 "7": "YediYuz",
 "8": "SekizYuz",
 "9": "DokuzYuz"}

text_list = ["", "Bin", "Milyon", "Milyar", "Trilyon"]


def number3(number):
    if len(number) == 1:
        my_string = d_birler[number[-1]]
    elif len(number) == 2:
        my_string = d_onlar[number[-2]] + d_birler[number[-1]]
    else:
        my_string = d_yuzler[number[-3]] + d_onlar[number[-2]] + d_birler[number[-1]]

    return my_string


def numberText(number):
    number = number.lstrip("0")
    if number == "":
        return "Sifir"
    my_string = ""
    i = 0
    while number:
        if int(number[-3:]) == 0:
            my_string = number3(number[-3:]) + my_string
        else:
            my_string = number3(number[-3:]) + text_list[i] + my_string
        number = number[:-3]
        i += 1
    if my_string[:6] == "BirBin":
        my_string = my_string[3:]

    return my_string

#print map(number3, ["123", "234", "643", "999", "10", "00001", "00000"])

assert number3("307") == "UcYuzYedi", "Beklenilen " + number3("307")
assert number3("007") == "Yedi", "Beklenilen " + number3("007")
assert number3("100") == "Yuz", "Beklenilen " + number3("100")
assert number3("999") == "DokuzYuzDoksanDokuz", "Beklenilen " + number3("999")
assert number3("213") == "IkiYuzOnUc", "Beklenilen " + number3("213")
assert number3("001") == "Bir", "Beklenilen " + number3("001")
assert number3("099") == "DoksanDokuz", "Beklenilen " + number3("099")
assert number3("500") == "BesYuz", "Beklenilen " + number3("500")
assert number3("999") == "DokuzYuzDoksanDokuz", "Beklenilen " + number3("999")
assert number3("01") == "Bir", "Beklenilen " + number3("01")


assert numberText("02") =="Iki", "Hatasi"
assert numberText("99999") =="DoksanDokuzBinDokuzYuzDoksanDokuz", "Sifir Hatasi"
assert numberText("1000") =="Bin", "Sifir Hatasi"
assert numberText("1000000000000") == "BirTrilyon", "Beklenilen: " + numberText("1000000000000")

while True:
    num = raw_input("Enter a number:")
    print numberText(num)





