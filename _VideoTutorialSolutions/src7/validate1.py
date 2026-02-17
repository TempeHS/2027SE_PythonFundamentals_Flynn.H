# Validates email address by checking for . too
#
# EXPLANATION:
# Adding another check - emails need both @ AND a dot!
#
# KEY CONCEPTS:
# - 'and' requires BOTH conditions to be True
# - Emails have format: username@domain.tld
# - The domain part needs a dot (like gmail.com)
#
# HOW IT WORKS:
# - Check for "@" in email AND "." in email
# - Both must be present for email to be "Valid"
#
# STILL LIMITED:
# These would still be "Valid" (but shouldn't be):
# - "@."           (just symbols)
# - ".@"           (wrong order)
# - "a.b@c"        (dot in wrong place)
#
# We need to be more specific about WHERE the @ and . appear.
# See validate2.py for splitting the email apart!

email = input("What's your email? ").strip()

if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")
