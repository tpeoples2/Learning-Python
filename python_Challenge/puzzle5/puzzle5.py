import pickle, urllib2

pickleFile = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")

unpickled = pickle.load(pickleFile)

for i in unpickled:
    print "".join([j[0] * j[1] for j in i])

#clue = []
#for i in range(0, len(unpickled)):
    #for j in range(0, len(unpickled[i])):
        #clue.append(unpickled[i][j][0] * unpickled[i][j][1])
    #clue.append("\n")
#print "".join(clue)

