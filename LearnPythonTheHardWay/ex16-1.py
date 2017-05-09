from sys import argv
script, filename=argv
print "Now we're going to read the file %s" % filename
txt=open(filename)
print txt.read()
txt.close()
