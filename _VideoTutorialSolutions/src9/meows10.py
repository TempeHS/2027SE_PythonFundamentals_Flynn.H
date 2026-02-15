# Uses Sphinx docstring format
#
# EXPLANATION:
# Detailed docstrings document parameters and return values!
#
# KEY CONCEPTS:
# - :param name: Description of parameter
# - :type name: Type of parameter
# - :return: What the function returns
# - :rtype: Return type
# - :raise ErrorType: What errors might be raised
#
# SPHINX FORMAT:
# Popular format used by Sphinx documentation generator.
# Creates beautiful HTML documentation from docstrings.
#
# THE DOCSTRING:
# :param n: Number of times to meow
# :type n: int
# :raise TypeError: If n is not an int
# :return: A string of n meows, one per line
# :rtype: str
#
# OTHER FORMATS:
# - Google style: Uses Args:, Returns: sections
# - NumPy style: Uses Parameters, Returns sections
# Pick one format and be consistent!


def meow(n):
    """
    Meow n times.

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """
    return "meow\n" * n


number = int(input("Number: "))
meows = meow(number)
print(meows, end="")
