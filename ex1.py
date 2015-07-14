print "hello world!"
print "hello again"
print "i like typing this"
#print "this is fun"
print "yay printing"
print "i'd much rather you 'not'"
print 'i "said" do not touch this'
print 3+2 < 5-7
print "What is 3 + 2?", 3 + 2
print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2
cars = 100
carSpace = 4.0
drivers = 30
passengers = 90
carsNotDriven = cars - drivers
carsDriven = drivers
carpoolCapacity = carsDriven * carSpace
avgPassengersPerCar = passengers / carsDriven

print "there are", cars, " cars available"
print "there are only", drivers, " driers available"

myName  = "MTrail"
print "lets talk %s" % myName
myAge = 41
print "my age %d" % myAge
print "my name is %s and i am %d" % (myName, myAge)

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.  try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

formatter = "%r %r %r %r"
print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")

age = raw_input("how old are you?")
height = raw_input("how tall are you?")

print "so, you are %r old and %r tall" % (age, height)