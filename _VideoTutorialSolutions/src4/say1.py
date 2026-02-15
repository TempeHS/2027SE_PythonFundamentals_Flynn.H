# Demonstrates a t-rex
#
# EXPLANATION:
# This program uses a different cowsay character - a T-Rex!
#
# KEY CONCEPTS:
# - cowsay has many different character functions
# - cowsay.trex() creates a T-Rex instead of a cow
# - Same message, different (and scarier) animal!
#
# HOW IT WORKS:
# Same as say0.py, but with cowsay.trex() instead of cowsay.cow()
#
# OTHER COWSAY CHARACTERS:
# - cowsay.cheese()
# - cowsay.dragon()
# - cowsay.kitty()
# - cowsay.stegosaurus()
# - cowsay.turtle()
# - cowsay.tux() (Linux penguin)
# - And many more!
#
# FUN FACT:
# cowsay originated as a command-line program in 1999.
# It's a classic example of "useless but fun" Unix culture.
# Sometimes programming should just be fun!

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])
