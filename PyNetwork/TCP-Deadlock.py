#!/usr/bin/env python
#TCP Client and Server that leave a lot of data waiting

import socket,sys

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = '127.0.0.1'
port = 8888

if sys.argv[1:] == ['server']:
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) 
	s.bind((host, port)) 
	s.listen(1) 
	while True:
		print 'Listening at', s.getsockname()
		sc,sockname= s.accept()
		print 'Processing up to 1024 bytes at a time from', sockname
		n=0
		while True:
			message = sc.recv(1024);
			if not message:
				break
			sc.sendall(message.upper()) #send it back in uppercase
			n += len(message) 
			print '\r %d bytes processed so far' %(n,),sys.stdout.flush() 
		print 
		sc.close()
		print 'Completed Processing'

elif len(sys.argv) == 3 and sys.argv[1] == 'client' and sys.argv[2].isdigit() : 
	bytes = (int(sys.argv[2])+15) // 16 * 16 #round up to //16
	message = 'capitalize this! ' #16-byte message to repeat over and over

	print 'Sending ',bytes,' bytes of data in chunks of 16 bytes'
	s.connect((host,port))

	sent=0
	while sent<bytes:
		s.sendall(message)
		sent += len(message) 
		print '\r %d bytes sent' %(sent,),sys.stdout.flush()
	print
	s.shutdown(socket.SHUT_WR) 

	print 'Receiving all the data the server sends back'
	
	received =0
	while True:
		data = s.recv(42)
		if not received:
			print 'The first data received says', repr(data)
		received += len(data)
		if not data:
			break
		print '\r %d bytes received' % (received,),
	s.close() 

else:
	print 'ERROR!'


