from sys import argv

script, input_file = argv

def printAll(f):
	print f.read()
	
def rewind(f):
	f.seek(0)
	
def printLine(lineCount, f):
	print lineCount, f.readline(),
	
current_file = open(input_file)

print "print whole file \n"
printAll(current_file)

print "rewinding"
rewind(current_file)

print "print three lines:"
currentLine = 1
printLine(currentLine,current_file)

currentLine = currentLine + 1
printLine(currentLine,current_file)

currentLine += 1
printLine(currentLine,current_file)

