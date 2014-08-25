 # coding: utf-8
import pprint
from copy import deepcopy

pokemans = """
bagon audino  baltoy banette bidoof braviary bronzor carracosta charmeleon
sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko
tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask
""".split()

"""
    veri tipi :
    {
        word: "yamask",
        starts_with: "y",
        ends_with: "k",
        branches: []
    }

    branches, bu nodedan sonra gelebilecek elemanların oluşturduğu bir liste
    [
        {
            word: "kangaskhan",
            starts_with: "k",
            ends_with: "n",
            branches: [...]
        },
        {
            word: "kricketune",
            starts_with: "k",
            ends_with: "e",
            branches: [...]
        }
    ]

    Bu şekilde herhangi bir elemandan başlayarak o elemanı takip eden olası
    elemanların oluşturduğu bir ağaç yapısı çıkartıyoruz.
"""


def make_node(word):
    return {
        "word": word,
        "starts_with": word[0],
        "ends_with": word[-1],
        "branches": []
    }


def make_index(items):
    d = {}
    for item in items:
        first_letter = item[0]
        if first_letter not in d:
            d[first_letter] = []
        d[first_letter].append(item)
    return d


def set_branches(node, index, ignore_list):
    for item in index.get(node["ends_with"], []):
        print ignore_list
        if item in ignore_list:
            continue
        temp_ignore_list = ignore_list + [item]
        index_copy = deepcopy(index)
        index_copy.get(node["ends_with"]).remove(item)

        branch = make_node(item)
        node["branches"].append(branch)
        set_branches(branch, index_copy, temp_ignore_list)


index = make_index(pokemans)
for word in pokemans:
    root = make_node(word)
    used_words = [word]
    set_branches(root, deepcopy(index), used_words)
