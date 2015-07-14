from sys import argv	
from os.path import exists

script, fromFile, toFile = argv

print "copying from %s to %s" % (fromFile, toFile)

inFile = open(fromFile)
inData = inFile.read()

print "input is %d bytes" % len(inData)

print "does the output exist ? %r" % exists(toFile)
print "hit return to continue"
raw_input()

outFile = open(toFile, 'w')
outFile.write(inData)

print "done"

outFile.close()
inFile.close()

