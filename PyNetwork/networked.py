# import socket

# #MAKE A SOCKET CONNECTION
# mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# mysock.connect(('www.py4inf.com',80))

# mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

# while True:
# 	data = mysock.recv(512)
# 	if (len(data) < 1 ):
# 		break
# 	print data 
# mysock.close()
 
# import urllib #makes URL seem like files.
# fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
# mhand = urllib.urlopen('http://www.azlyrics.com/lyrics/megadeth/tornadoofsouls.html')
# for line in fhand:
# 	print line.strip()
# 	# print line 
# for line in mhand:
# 	print line.strip()

# counts = dict()
# for line in fhand:
# 	words = line.split()
# 	for word in words:
# 		counts[word] = counts.get(word,0)+1
# print counts 

