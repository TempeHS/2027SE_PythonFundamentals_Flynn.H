# Demonstrates shuffle
#
# EXPLANATION:
# This program randomly shuffles a list - like shuffling a deck of cards!
#
# KEY CONCEPTS:
# - random.shuffle(list) randomly reorders the items in place
# - "In place" means it modifies the original list (doesn't return a new one)
# - After shuffling, the cards will be in a random order
#
# HOW IT WORKS:
# 1. cards = ["jack", "queen", "king"] - original order
# 2. random.shuffle(cards) - shuffles in place (might become ["king", "jack", "queen"])
# 3. for loop prints each card in the new random order
#
# IN-PLACE VS RETURN:
# Some functions modify the original object (in place):
#   list.sort(), list.reverse(), random.shuffle()
#
# Others return a new object:
#   sorted(list), reversed(list)
#
# Be aware of which type you're using!
#
# USE CASES:
# - Card games: Shuffle the deck
# - Quiz apps: Randomize question order
# - Playlists: Shuffle songs
# - Testing: Randomize test data

import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
