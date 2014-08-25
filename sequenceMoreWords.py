text = """
audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon
cresselia croagunk darmanitan deino emboar emolga exeggcute gabite
girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan
kricketune landorus ledyba loudred lumineon lunatone machamp magnezonemamoswine
nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2
porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking
sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko
tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask
"""
word_list = text.split()
word_tuple_list = []
start_letters = {}
my_list = []


for w in word_list:
    first = list(w)[0]
    last = list(w)[len(w) - 1]

    if first in start_letters:  # Creating first_letters numbers dictionary
        start_letters[first] = int(start_letters[first]) + 1
    else:
        start_letters[first] = 1

    word_tuple_list.append((w, first, last))


def make_sequence_from_tuple(all_words_tuple):
    temp = all_words_tuple
    max_number = 0
    my_word = None
    while True:
        for w, f, l in temp:
            if l in start_letters and start_letters[l] > max_number:
                more_used_letter = l
                max_number = start_letters[l]
                my_word = w
        if my_list and my_word == my_list[-1]:
            break
        max_number = 0
        my_list.append(my_word)
        for t in all_words_tuple:
            if my_word in t:
                all_words_tuple.remove(t)
        temp = []
        for w, f, l in all_words_tuple:
            if f == more_used_letter:
                temp.append((w, f, l))
    return my_list

print "\n", make_sequence_from_tuple(word_tuple_list)
print "\n%s words are sequenced systematically" % len(my_list)
