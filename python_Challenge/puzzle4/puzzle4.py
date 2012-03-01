import urllib2
import re

link_base = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

text = urllib2.urlopen(link_base + str(12345)).read()
number = re.findall("\d+", text)

while len(number) is not 0:
    text = urllib2.urlopen(link_base + number[0]).read()
    print text
    number = re.findall("\d+", text)

print "Can't go any farther."
