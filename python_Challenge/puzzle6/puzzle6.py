import re
import zipfile

zippedFile = zipfile.ZipFile("channel.zip", "r")

file_prefix = "readme"
file_suffix = ".txt"
text = zippedFile.read(file_prefix + file_suffix)
number = re.findall("\s(\d+)", text)

history = []
while len(number) is not 0:
    history.append(number[0])
    file_prefix = number[0]
    text = zippedFile.read(file_prefix + file_suffix)
    print text
    number = re.findall("\s(\d+)", text)

print "".join([(zippedFile.getinfo(prefix + file_suffix)).comment for prefix in history])

