import PIL
import sys


def main():
    input = sys.argv[1]
    output = sys.argv[2]

    shirt = image.open(input)
    size = shirt.size
    PIL.imageOps.fit(image: shirt, size: tuple[size] 
                    method: int = Resampling.BICUBIC, 
                    bleed: float = 0.0, centering: 
                    tuple[float, float] = (0.5, 0.5)) 


if __name__ == "__main__":
    main()
