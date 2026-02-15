# Adds default, type; removes int()
#
# EXPLANATION:
# argparse can handle type conversion and defaults!
#
# KEY CONCEPTS:
# - default=1: Use 1 if -n not provided
# - type=int: Automatically convert to int
# - No need for int(args.n) - already converted!
#
# THE CODE:
# parser.add_argument("-n", default=1, help="...", type=int)
#
# BENEFITS:
# - type=int: argparse converts for you
# - default=1: Program works without -n
# - Error message if value can't be converted
#
# USAGE:
# python meows14.py        # Uses default, meows once
# python meows14.py -n 3   # Meows 3 times
# python meows14.py -n abc # Error: invalid int value
#
# OTHER TYPES:
# type=float, type=str (default), or custom functions!

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("meow")
