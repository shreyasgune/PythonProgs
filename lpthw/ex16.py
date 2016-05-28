from sys import argv

script, filename = argv

print "We're going to erase %r" % filename
print "If you don't want that , hit CTRL-C (^c)"
print "If you do , hit ENTER"

raw_input("?")

print "Opening the fie..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now add three lines , plej"

line1 = raw_input("line 1 :")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I am going to write these to the file"

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print "And we finally close.."
target.close()
