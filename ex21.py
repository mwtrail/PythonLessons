def add(a, b):
	print "adding %d + %d" % (a,b)
	return a + b
	
def subtract(a,b):
	print "subtract %d - %d" % (a,b)
	return a-b

def multiply(a,b):
	print "multiply %d * %d" % (a,b)
	return a*b

def divide(a,b):
	print "divide %d / %d" % (a,b)
	return a/b

print "lets do math"
age = add(30,5)
height = subtract(65,6)
weight = multiply(5,40)
iq = divide(100,2)

print "age: %d, height: %d, weight: %d, iq: %d" %(age, height,weight,iq)

print "puzzle"
what = add(age, subtract(height, multiply(weight,divide(iq,2))))

print "that becomes ", what, "can you do it?"