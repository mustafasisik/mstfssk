# coding: utf-8
bir = {"0": "",
 "1": "Bir",
 "2": "Iki",
 "3": "Uc",
 "4": "Dort",
 "5": "Bes",
 "6": "Alti",
 "7": "Yedi",
 "8": "Sekiz",
 "9": "Dokuz"}

on = {"0": "",
 "1": "On",
 "2": "Yirmi",
 "3": "Otuz",
 "4": "Kirk",
 "5": "Elli",
 "6": "Altmis",
 "7": "Yetmis",
 "8": "Seksen",
 "9": "Doksan"}

step = ["Trilyon", "Milyar", "Milyon", "Bin"]


def read(number):
    if number == "":
        return ""
    elif int(number) == 0:
        return "Sifir"
    else:
        num = number[-3:].lstrip("0")
        if len(num) == 1:
            my_string = bir[num[-1]]
        elif len(number) == 2:
            my_string = on[num[-2]] + bir[num[-1]]
        elif num[-3] == "1":
            my_string = "Yuz" + on[num[-2]] + bir[num[-1]]
        else:
            my_string = bir[num[-3]] + "Yuz" + on[num[-2]] + bir[num[-1]]
        number = number[:-3]
        if number != "":
            return read(number) + "Bin" + my_string
        else:
            return my_string

print read("1")
print read("122312")
print read("123")


assert read("131") == "YuzOtuzBir", "Beklenen: " + read("131")
assert read("000") == "Sifir", "Beklenen: " + read("000")
assert read("001") == "Bir", "Beklenen: " + read("001")
assert read("999") == "DokuzYuzDoksanDokuz", "Beklenen: " + read("999")
assert read("231") == "IkiYuzOtuzBir", "Beklenen: " + read("231")
assert read("990") == "DokuzYuzDoksan", "Beklenen: " + read("990")
assert read("000") == "Sifir", "Beklenen: " + read("000")
assert read("01") == "Bir", "Beklenen: " + read("01")
assert read("1") == "Bir", "Beklenen: " + read("1")
#assert read("1234324") == "BirMilyonIkiYuzOtuzDortBinUcYuzYirmiDort", "Beklenen: " + read("1234324")




