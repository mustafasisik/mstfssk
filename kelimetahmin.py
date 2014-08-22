#coding: utf-8
my_word = "deneme"

print "------"
inp = raw_input("bir harf giriniz:")


def find_index_of_letter(word, letter):
    if letter in word:
        return word.index(letter)

print find_index_of_letter(my_word, inp)
