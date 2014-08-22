#coding: utf-8
from sys import argv
my_word = argv[1]
letter_list = ["_"] * len(my_word)

print " ".join(letter_list)

while "_" in letter_list:
    inp = raw_input("bir harf giriniz:")
    for a, b in enumerate(my_word):
        if b == inp:
            letter_list[a] = inp
    print " ".join(letter_list)
print("Well Done")
