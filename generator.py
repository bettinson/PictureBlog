import os
from PIL import Image


def get_directory_names():
    directory_names = []
    for picture in os.listdir("pictures/"):
        if picture:
            directory_names.append("pictures/" + picture)

    return directory_names


pictures = get_directory_names()

# The first picture, because the [0] element is .DS_Store

base_picture = Image.open(pictures[1])
base_width_height = base_picture.size

print base_width_height

html = ""

for src in get_directory_names():
    if src != "pictures/.DS_Store":
        html += '<img src="' + src + '">' + "\n"

f = open("index.html", "w")

f.write(html)
f.close()