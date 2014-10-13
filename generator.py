import os
from PIL import Image


def get_directory_names():
    directory_names = []
    for picture in os.listdir("Pictures/"):
        if picture:
            directory_names.append("Pictures/" + picture)

    return directory_names

pictures = get_directory_names()

# The first picture, because the [0] element is .DS_Store
# TODO: REGEX for pictures

base_picture = Image.open(pictures[1])
base_width_height = base_picture.size

page_title = pictures[0][0:8]

width = str(base_width_height[0] * 0.2)

print base_width_height

html = "<center><h1>" + page_title + "</h1></center>"

for src in get_directory_names():
	if src != "Pictures/.DS_Store":
		picture_name = src[9:]
		picture_name =  picture_name[0:len(picture_name) - 4]
        	html += '<center><img src="' + src + '" width =' + width + ' ></center> <center><h2>' + picture_name + '</center></h2><br>' + "\n"

f = open("index.html", "w")

f.write(html)
f.close()
