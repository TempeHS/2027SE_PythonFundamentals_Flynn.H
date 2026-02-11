# Uses command-line argument
#
# EXPLANATION:
# argparse makes command-line parsing easy!
#
# KEY CONCEPTS:
# - ArgumentParser(): Creates a parser
# - add_argument("-n"): Defines an option
# - parse_args(): Parses sys.argv automatically
# - args.n: Access the parsed value
#
# THE CODE:
# parser = argparse.ArgumentParser()
# parser.add_argument("-n")
# args = parser.parse_args()
# args.n  # The value of -n
#
# USAGE:
# python meows12.py -n 3
#
# BENEFITS:
# - Automatic parsing of -n 3
# - Handles spaces: -n 3 or --n=3
# - Error messages for invalid input
#
# See meows13.py for descriptions and help!

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n")
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")
