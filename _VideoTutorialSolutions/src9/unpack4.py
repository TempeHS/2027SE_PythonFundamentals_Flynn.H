# Passes named arguments as usual
#
# EXPLANATION:
# NAMED ARGUMENTS specify which parameter gets which value!
#
# KEY CONCEPTS:
# - galleons=100: Explicitly names the parameter
# - Order doesn't matter with named arguments
# - Self-documenting - clear what each value means
#
# POSITIONAL VS NAMED:
# Positional: total(100, 50, 25)  # Order matters!
# Named: total(knuts=25, galleons=100, sickles=50)  # Order doesn't matter!
#
# WHY USE NAMED:
# - Code is clearer: what's 100? galleons!
# - Can reorder parameters
# - Can skip optional parameters
#
# See unpack5.py for passing values from a dict!


def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


print(total(galleons=100, sickles=50, knuts=25), "Knuts")
