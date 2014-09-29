import os
from PIL import Image


def get_directory_names():
    directory_names = []
    for picture in os.listdir("pictures/"):
        if picture:
            directory_names.append("pictures/" + picture)

    return directory_names

html = ""

pictures = get_directory_names()
base_picture = Image.open(pictures[0])
#base_width_height = base_picture.size

for src in get_directory_names():
    if src != ".DS_Store":
        html += '<img src="' + src + '">' + "\n"

f = open("index.html", "w")

f.write(html)
f.close()
