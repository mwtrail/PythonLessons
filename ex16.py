from sys import argv	

script, filename = argv

# txt = open(filename)
# print "here is your file %r : " % filename
# print txt.read()

# print "type file name again"
# file_again = raw_input(">")

#txtagain = open(file_again)
# print txtagain.read()


print "we are going to erase %r" % filename
print "if you want that , hit return"
raw_input ("?")

print "opening file.."
target = open(filename, 'w')

print "truncating file"
target.truncate()

print "asking for three lines"
line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "writing to the file"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "close the file"
target.close()
