from PIL import Image
import os, glob

'''
PIL: Python Imaging Library

Concepts:
- very large module, good to import only what you need
'''
size = 128, 128

for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    print(file, ext, infile)
    print(infile)

    with Image.open(infile) as im:
        im.thumbnail(size)
        im.save(file + ".png", "PNG")


# # with open to ensure file is closed
# with Image.open("new-york.jpg") as im:
#     print(im.size)
#     print(im.format)
#     # im.rotate(45).show
