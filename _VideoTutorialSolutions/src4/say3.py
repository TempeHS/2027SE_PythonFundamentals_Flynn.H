# Demonstrates own module
#
# EXPLANATION:
# This program imports from sayings1.py, which has a main() function.
#
# KEY CONCEPTS:
# - Same as say2.py, but sayings1.py has a different structure
# - sayings1.py calls main() at the end of the file
# - When you import from sayings1, it runs main() as a side effect!
# - This is usually NOT what you want!
#
# THE PROBLEM:
# sayings1.py ends with: main()
# When Python imports sayings1, it runs ALL the code in that file,
# including the main() call!
#
# So running: python say3.py David
# First prints: "hello, world" and "goodbye, world" (from sayings1.py)
# Then prints: "hello, David" (from say3.py)
#
# THE SOLUTION:
# See sayings2.py for the fix using: if __name__ == "__main__"
# This prevents main() from running when the module is imported.

import sys

from sayings1 import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])
