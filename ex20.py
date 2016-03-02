from sys import argv

script, input_file = argv #take the file on console input

def print_all(f):
	print f.read()   #f is a predefined object for the file.

def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file.\n"
print_all(current_file)

print "Now let us rewind the file, like a tape.\n"
rewind(current_file)

print "Let us print three lines:"

current_line = 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)

"""
PS C:\lpthw> python ex20.py text_file.txt
First let's print the whole file.

This is Limp Bizkit
They released an album in 2005.
It was called , 'The Unquestionable Truth , Part I'
Now let us rewind the file, like a tape.

Let us print three lines:
1 This is Limp Bizkit

2 They released an album in 2005.

3 It was called , 'The Unquestionable Truth , Part I'
"""