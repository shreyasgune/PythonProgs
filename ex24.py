print "Lets practice everything we know."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
is just a deceptive facade
to hid the base inequities of life
\n\t\twhere there is none.
"""
print "--------------"
print poem
print "--------------"

five = 10-2+3-6
print "This should be five: %s" %five

def secret_formula(started):
	jelly_beans = started*500
	jars = jelly_beans/1000
	crates = jars/100
	return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point) #you can instantiate variables with data by passing a arg within a fucntion call

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates" %(beans,jars,crates)

start_point = start_point/10

print "We can also do it this way:"
print "we'd have %d beans, %d jars, and %d crates." %secret_formula(start_point)

