import urllib2
from PIL import Image
import re

picture = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/oxygen.png").read()

oxygen = open("oxygen.png", "wr")
oxygen.write(picture)
oxygen.close()

image = Image.open("oxygen.png")
rgb_values = []
for i in range(0, image.size[0], 7):
    rgb_values.append(image.getpixel((i, 43))[0])

clue = "".join(map(chr, rgb_values))

nums = re.findall("\d{3}", clue)
print "".join([chr(int(num)) for num in nums])

