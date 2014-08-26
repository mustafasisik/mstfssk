#coding: UTF-8

onlar_basamagi = {"0": "", "1":"On", "2":"Yirmi", "3":"Otuz", "4":"Kirk", "5":"Elli", "6":"Altmis", "7":"Yetmis", "8":"Seksen", "9": "Doksan"}

birler_basamagi = {"0": "Sifir", "1":"Bir", "2":"iki", "3":"Uc", "4":"Dort", "5":"Bes", "6":"Alti", "7":"Yedi", "8":"Sekiz", "9": "Dokuz"}

step_dictionary = {"3": "bin", "6": "milyon", "9": "milyar", "12": "trilyon"}


def numberText(number):
    string_number_list = list(str(number))[::-1]
    my_number_list = []
    step = 0
    while string_number_list:
        step += 1
        if step % 3 == 2:
            my_number_list.append(onlar_basamagi[string_number_list[0]])
        else:
            my_number_list.append(birler_basamagi[string_number_list[0]])
        string_number_list.remove(string_number_list[0])
        if step % 3 == 2:
            my_number_list.append("Yuz")
        if step % 3 == 0:
            my_number_list.append(step_dictionary[str(step)])
    print " ".join(my_number_list[::-1])



numberText(1234638451754)
