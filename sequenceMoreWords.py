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
end_letters = {}
my_list = []

for w in word_list:
    first = list(w)[0]
    last = list(w)[len(w) - 1]

    if first in start_letters:  # Creating first_letters numbers dictionary
        start_letters[first] = int(start_letters[first]) + 1
    else:
        start_letters[first] = 1

    if last in end_letters:  # Creating end_letters numbers dictionary
        end_letters[last] = int(end_letters[last]) + 1
    else:
        end_letters[last] = 1


for w in word_list:  # Creating a tuple list for each word
    f = list(w)[0]
    l = list(w)[len(w) - 1]
    word_tuple_list.append((w, f, l))

print word_tuple_list

for w, f, l in word_tuple_list:    # finding most used letter
    max_number = 0
    if l in start_letters:
        if start_letters[l] >= max_number:
            most_used_letter = l
            max_number = start_letters[l]
print most_used_letter


temp_list = []
for w, f, l in word_tuple_list:
    if w.startswith(most_used_letter):
        t = (w, f, l)
        temp_list.append(t)

print temp_list
