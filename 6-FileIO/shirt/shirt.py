from PIL import Image, ImageOps
import sys
from pathlib import Path


def main():

    if len(sys.argv) > 3:
        sys.exit("Must include an input and output file")
    if len(sys.argv) < 3:
        sys.exit("Must include an input and output file")

    input = Path(sys.argv[1])
    output = Path(sys.argv[2])
    input = input.lower()
    output = output.lower()
    try:
        with Image.open(input) as input, Image.open("shirt.png") as shirt:
            size = shirt.size
            fitted = ImageOps.fit(input, size)
            fitted.paste(shirt, (0, 0), shirt)
            fitted.save(output)
    except (FileNotFoundError, ValueError):
        sys.exit("file could not be found")


if __name__ == "__main__":
    main()
