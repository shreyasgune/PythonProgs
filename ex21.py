def add(a,b):
	print "ADDING %d + %d" %(a,b)
	return a+b

def sub(a,b):
	print "SUBTRACTING %d - %d" %(a,b)
	return a-b

def mul(a,b):
	print "Multiplying %d * %d " %(a,b)
	return a*b

def div(a,b):
	print "Dividing %d / %d " %(a,b)
	return a/b


print "Let's do some math"

age= add(20,5)
height = sub(178,3)
weight = mul(8,10)
iq = div(300,2)


print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

#A puzzle for extra credit

print "Here is a puzzle"

what= add(age,sub(height,mul(weight,div(iq,2))))
print "That becomes : ", what, "can you do it by hand?"


"""
Let's do some math
ADDING 20 + 5
SUBTRACTING 178 - 3
Multiplying 8 * 10
Dividing 300 / 2
Age: 25, Height: 175, Weight: 80, IQ: 150
Here is a puzzle
Dividing 150 / 2
Multiplying 80 * 75
SUBTRACTING 175 - 6000
ADDING 25 + -5825
That becomes :  -5800 can you do it by hand?

"""

