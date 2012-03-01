import re
from PIL import Image, ImageDraw

first = re.findall("\d+", open("first", "r").read())
second = re.findall("\d+", open("second", "r").read())

first = [int(i) for i in first]
second = [int(i) for i in second]

image = Image.new("RGB", (500, 500))
draw = ImageDraw.Draw(image)
draw.line(first)
draw.line(second)

image.show()

