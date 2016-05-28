from sys import argv #command line stuff

script, filename = argv #script takes command line inputs
txt = open(filename) #reference to the file

print "here is your file %r:" % filename
print txt.read()

print "the filename again please:?"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
