# Demonstrates own module
#
# EXPLANATION:
# This program imports from sayings2.py, which properly uses __name__.
#
# KEY CONCEPTS:
# - sayings2.py uses: if __name__ == "__main__": main()
# - This means main() only runs when sayings2.py is run directly
# - When imported, main() does NOT run - just the functions are available
# - This is the correct pattern for reusable modules!
#
# THE MAGIC OF __NAME__:
# When a file is run directly: __name__ == "__main__"
# When a file is imported: __name__ == "module_name" (e.g., "sayings2")
#
# EXAMPLE:
# python sayings2.py -> __name__ == "__main__" -> runs main()
# from sayings2 import hello -> __name__ == "sayings2" -> doesn't run main()
#
# This pattern is extremely common in Python!
# It allows a file to be both:
# 1. A runnable program (when run directly)
# 2. An importable module (when imported by other files)

import sys

from sayings2 import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])
