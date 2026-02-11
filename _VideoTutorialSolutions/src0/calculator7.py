# Demonstrates formatting with commas
#
# EXPLANATION:
# This program shows how to format large numbers with commas for readability.
#
# KEY CONCEPTS:
# - F-strings can include format specifiers after a colon
# - {z:,} tells Python to format z with comma separators
# - 1000000 becomes "1,000,000" - much easier to read!
# - The comma is a "format specification" that groups digits by thousands
#
# HOW IT WORKS:
# 1. User enters large numbers (e.g., 1000000 and 2000000)
# 2. z = round(3000000)
# 3. f"{z:,}" formats z with commas: "3,000,000"
# 4. Output: 3,000,000
#
# FORMAT SPECIFIERS IN F-STRINGS:
# - {value:,} -> adds commas: 1000000 -> "1,000,000"
# - {value:.2f} -> 2 decimal places: 3.14159 -> "3.14"
# - {value:10} -> pads to 10 characters wide
# - {value:>10} -> right-align in 10 characters
# - {value:<10} -> left-align in 10 characters
#
# COMBINING FORMATS:
# - {value:,.2f} -> commas AND 2 decimal places: 1234567.891 -> "1,234,567.89"
#
# This is especially useful for displaying money or large statistics!

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

print(f"{z:,}")
