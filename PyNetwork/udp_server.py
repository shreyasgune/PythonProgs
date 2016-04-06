import sys,socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

MAX = 65535
PORT = 1060

# test = open('test.html')
# txt = test.read()

if sys.argv[1:] == ['server']:
	s.bind(('127.0.0.1',PORT))
	print 'Listening at' ,s.getsockname()
	while True:
		data,address = s.recvfrom(MAX)
		print 'The client at',address,'says',repr(data)
		s.sendto('Your data was %d bytes' %len(data),address)

elif sys.argv[1:] == ['client']:
	#print 'Address b4 sending: ' ,(s.getsockname())
	s.sendto('whatever', ('127.0.0.1',PORT))
	print 'Address after sending: ' ,s.getsockname()
	data,address = s.recvfrom(MAX)
	print 'The Server',address , 'says', repr(data)

else:
	print sys.stderr, 'usage: udp_server.py server|client'


''' OUTPUT
client::
C:\dev\PyNetwork>python udp_server.py client
Address after sending:  ('0.0.0.0', 64393)
The Server ('127.0.0.1', 1060) says 'Your data was 18 bytes'

C:\dev\PyNetwork>python udp_server.py client
Address after sending:  ('0.0.0.0', 64394)
The Server ('127.0.0.1', 1060) says 'Your data was 18 bytes'

Server::
Listening at ('127.0.0.1', 1060)
The client at ('127.0.0.1', 64393) says 'This is my message'
The client at ('127.0.0.1', 64394) says 'This is my message'
'''
