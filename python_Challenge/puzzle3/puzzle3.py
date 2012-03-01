text = open("puzzle3txt").read()

import re

hits = re.findall("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]", text)
print "".join(hits)
