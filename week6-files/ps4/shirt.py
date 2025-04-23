import sys

import PIL
from PIL import Image , ImageOps

if len(sys.argv) == 1:
    print("Too few command-line arguments")
    sys.exit(1)

if len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)


def is_valid(img):
    formats = ("png","jpg","jpeg","gif")
    for format_name in formats:
        if img.endswith(format_name):
            return True
        else:
            continue

    return False

if not is_valid(sys.argv[2]):
    print("Invalid output")
    sys.exit(1)

img_name1,extention1 = sys.argv[1].split(".")
img_name2,extention2 = sys.argv[2].split(".")

if extention1 != extention2:
    print("Input and output have different extensions")
    sys.exit(1)



try:
    filename = "shirt.png"
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]







except FileNotFoundError:
    print("File Not Found Error")
    sys.exit(1)

except PIL.UnidentifiedImageError:
    print("Image can not be Identified and open")
    sys.exit(1)

except ValueError:
    print("Not Correct Mode")
    sys.exit(1)

except TypeError:
    print("Format is Not None.")
    sys.exit(1)



