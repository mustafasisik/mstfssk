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


def letters_used_at_start(liste):
    for w in liste:
        c = list(w)[0]

        if c in start_letters:
            start_letters[c] = int(start_letters[c]) + 1
        else:
            start_letters[c] = 1
    return start_letters
start_letters = letters_used_at_start(word_list)


def letter_used_at_least(liste):
    for w in liste:
        c = list(w)[len(w) - 1]
        if c in end_letters:
            end_letters[c] = int(end_letters[c]) + 1
        else:
            end_letters[c] = 1
    return end_letters
end_letters = letter_used_at_least(word_list)


def create_word_tuple_list(liste):
    for w in liste:
        f = list(w)[0]
        l = list(w)[len(w) - 1]
        word_tuple_list.append((w, f, l, start_letters[f], end_letters[l]))
    return word_tuple_list
word_tuple_list = create_word_tuple_list(word_list)


my_word = word_tuple_list[0][0]
max_number = word_tuple_list[0][3]
my_letter = word_tuple_list[0][1]

for w, f, l, fn, ln in word_tuple_list:    # finding most used letter
    if fn >= max_number:
        most_used_letter = f
        max_number = fn
print most_used_letter


def find_most_used_letter_end_of_word(liste):
    my_letter = None
    max_number = 0
    for l in liste:
        if start_letters[l] > max_number:
            my_letter = l
            max_number = start_letters[l]
    return my_letter


temp_list = []
for w, a, b, c, d in word_tuple_list:
    if w.startswith(most_used_letter):
        t = (w, a, b, c, d)
        temp_list.append(t)

print temp_list

print find_most_used_letter_end_of_word(temp_list)
