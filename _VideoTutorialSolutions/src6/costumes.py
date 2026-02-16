# Opens and saves binary files
#
# EXPLANATION:
# This creates an animated GIF from image files using Pillow (PIL)!
#
# KEY CONCEPTS:
# - PIL (Pillow) is a library for image processing
# - Image.open(filename) opens an image file
# - Images are BINARY files (not text)
# - save() with options creates animated GIFs
#
# HOW IT WORKS:
# 1. Loop through command-line arguments (image filenames)
# 2. Open each image with Image.open()
# 3. Add to images list
# 4. Save as animated GIF with special options
#
# USAGE:
# python costumes.py costume1.gif costume2.gif
# Creates: costumes.gif (animated, switching between the two)
#
# SAVE() OPTIONS:
# - save_all=True: Include all frames (for animation)
# - append_images=[...]: Additional frames to add
# - duration=200: Each frame shows for 200 milliseconds
# - loop=0: Loop forever (0 = infinite)
#
# BINARY VS TEXT FILES:
# Text: .txt, .csv, .py - human readable
# Binary: .gif, .png, .jpg, .exe - machine readable
#
# INSTALL PILLOW:
# pip install Pillow

import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)
