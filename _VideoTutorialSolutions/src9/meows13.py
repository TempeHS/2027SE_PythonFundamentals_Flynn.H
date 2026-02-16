# Adds description, help
#
# EXPLANATION:
# argparse can generate helpful usage information!
#
# KEY CONCEPTS:
# - description="...": Shown at top of --help
# - help="...": Describes what each argument does
# - python script.py --help shows all options
#
# THE CODE:
# parser = argparse.ArgumentParser(description="Meow like a cat")
# parser.add_argument("-n", help="number of times to meow")
#
# RUNNING WITH --HELP:
# $ python meows13.py --help
# usage: meows13.py [-h] [-n N]
#
# Meow like a cat
#
# optional arguments:
#   -h, --help  show this help message and exit
#   -n N        number of times to meow
#
# PROFESSIONAL TOUCH:
# Good help text makes your program user-friendly!
#
# See meows14.py for default values and types!

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", help="number of times to meow")
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")
