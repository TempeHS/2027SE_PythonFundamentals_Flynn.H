# Demonstrates formatting after the decimal place
#
# EXPLANATION:
# This program uses f-string formatting to display a specific number of decimal places.
#
# KEY CONCEPTS:
# - {z:.2f} formats z as a float with exactly 2 decimal places
# - .2 means "2 digits after the decimal point"
# - f means "format as floating-point"
# - Unlike round(), this always shows 2 decimal places, even if zeros
#
# HOW IT WORKS:
# 1. User enters integers (e.g., 10 and 4)
# 2. z = 10 / 4 = 2.5
# 3. f"{z:.2f}" formats as "2.50" (always 2 decimal places)
# 4. Output: 2.50
#
# ROUND() VS F-STRING FORMATTING:
# round(2.5, 2) = 2.5 (displays as 2.5, not 2.50)
# f"{2.5:.2f}" = "2.50" (always shows 2 decimal places)
#
# The f-string approach is better for consistent formatting (like currency).
#
# MORE EXAMPLES:
# - f"{3.14159:.3f}" = "3.142"
# - f"{3:.2f}" = "3.00"
# - f"{12345.678:.1f}" = "12345.7"
#
# COMBINING FORMAT SPECIFIERS:
# - f"{value:,.2f}" -> comma separators AND 2 decimals: "1,234.56"
# - f"{value:>10.2f}" -> right-aligned, 10 chars wide, 2 decimals

x = int(input("What's x? "))
y = int(input("What's y? "))

z = x / y

print(f"{z:.2f}")
