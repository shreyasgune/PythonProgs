from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#doing this in one line.
in_file= open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file even exist? %r" %exists(to_file)
print "Ready, hit ENTER to continue , ctrl-C to abort"
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright. All done."

out_file.close()
in_file.close()

"""
PS C:\lpthw> python ex12.py text_file.txt
We are going to erase 'text_file.txt'.
If you dont want that, hit ctrl-c
If you do want that , press ENTER
?
opening the file...
Truncating the file. Goodbye!
Now I'm going to ask you for three lines.
line 1: This is Limp Bizkit
line 2: They released an album in 2005.
line 3: It was called , 'The Unquestionable Truth , Part I'
I'm going to write these to the file.
PS C:\lpthw> python ex13.py text_file.txt new_file.txt
Copying from text_file.txt to new_file.txt
The input file is 103 bytes long
Does the output file even exist? True
Ready, hit ENTER to continue , ctrl-C to abort
""" 