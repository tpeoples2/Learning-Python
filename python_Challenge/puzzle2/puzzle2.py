text = open("puzzle2txt", "r").read()

rare = [char for char in text if text.count(char) < 5]

print "".join(rare)


