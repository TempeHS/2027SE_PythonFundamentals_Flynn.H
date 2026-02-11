# Success
#
# EXPLANATION:
# Now meow RETURNS a string instead of printing!
#
# KEY CONCEPTS:
# - def meow(n: int) -> str: returns a string
# - return "meow\n" * n: Returns string of meows
# - Caller controls what to do with the result
#
# THE CHANGE:
# Before: print("meow") inside function (side effect)
# After: return "meow\n" * n (pure function)
#
# STRING MULTIPLICATION:
# "meow\n" * 3 = "meow\nmeow\nmeow\n"
# Repeats the string n times!
#
# BENEFITS OF RETURNING:
# - Caller decides how to use the result
# - Can save to variable, print, write to file, etc.
# - Easier to test - check return value
#
# print(meows, end="") avoids extra newline.


def meow(n: int) -> str:
    return "meow\n" * n


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")
