# Demonstrates cowsay and text-to-speech
#
# EXPLANATION:
# Fun libraries for creative output!
#
# KEY CONCEPTS:
# - cowsay: ASCII art of animals saying things
# - pyttsx3: Text-to-speech (reads text aloud)
# - Combining libraries for fun effects!
#
# COWSAY:
# cowsay.cow("Hello") prints:
#   _______
#  < Hello >
#   -------
#         \   ^__^
#          \  (oo)\_______
#             (__)\       )\/\
#                 ||----w |
#                 ||     ||
#
# PYTTSX3:
# engine = pyttsx3.init()  # Create speech engine
# engine.say(text)         # Queue text to speak
# engine.runAndWait()      # Actually speak it
#
# FUN LIBRARIES:
# Python has libraries for almost everything!
# Explore and have fun!
import cowsay
import pyttsx3

engine = pyttsx3.init()
this = input("What's this? ")
cowsay.cow(this)
engine.say(this)
engine.runAndWait()
