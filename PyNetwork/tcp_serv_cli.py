
#!/usr/bin/env python
#A simple TCP client/server program that recieves/sends 16 bytes of data

import socket,sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#AF_INET is the IPv4 family, and SOCK_STREAM is the TCP mode

if(len(sys.argv)==3):
	host = sys.argv.pop()
else:
	host = '127.0.0.1'

port = 8888

def recv_all(sock, length):
	data=''
	while len(data) < length:
		more= sock.recv(length-len(data)) 
		if not more:
			raise EOFError('socket closed %d bytes into a %d-byte message' %(len(data),length)) 

		data += more
	return data

if sys.argv[1:] == ['server']:
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
	s.bind((host, port))
	s.listen(1)
	
	while True:
		print 'Listening at', s.getsockname()
		sc, sockname = s.accept()
		print 'We have accepted a connection from',sockname
		print 'Socket connects',sc.getsockname(),'and',sc.getpeername()
		message = recv_all(sc,16) #this specifies that I want only 16 bytes of data
		print 'The incoming 16 bytes message says', repr(message)
		sc.sendall('Farewell, client')
		sc.close()
		print 'Reply sent, socket closed'

elif sys.argv[1:] == ['client']:
	s.connect((host, port))
	print 'Client has been assigned socket name', s.getsockname()
	s.sendall('Hi there, server')
	reply = recv_all(s,16)
	print 'The server said',repr(reply)
	s.close() 
else:
	print>>sys.stderr,'usage:tcp_serv_cli.py server or client host address '


'''                                                                                      
you cannot simply call send() on a stream socket without checking the return value. 
Instead, you have to put a send() call inside a loop like this one, that in the case of
a partial transmission,keeps trying to send the remaining data until the entire string
has been sent every time we have a block of data to send,
the Standard Library socket implementation provides a friendly sendall() method. 
Not only is sendall() faster than doing it ourselves because it is implemented in C,
but it releases the Global Interpreter Lock during its loop so that other Python threads can run without contention until all of the data has been transmitted'''


	
