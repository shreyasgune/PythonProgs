#!/usr/bin/env python

#Broadcast Test using UDP

import sys, socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1) 

'''otes
value = s.getsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, value)

Many options are specific to particular operating systems, and may be finicky about how their options are presented. Here are some of the more common:

SO_BROADCAST: Allows broadcast UDP packets to be sent and received; see the next
section for details.


SO_DONTROUTE: Only be willing to send packets that are addressed to hosts on
subnets to which this computer is connected directly. My laptop, for example, at
this moment would be willing to send packets to the networks 127.0.0.0/8 and
192.168.5.0/24 if this socket option were set, but would not be willing to send
them anywhere else.

SO_TYPE: When passed to getsockopt(), this returns to you regardless of whether a
socket is of type SOCK_DGRAM and can be used for UDP, or it is of type SOCK_STREAM
and instead supports the semantics of TCP
'''

MAX = 65535
PORT= 1060

if sys.argv[1] == 'server':
	s.bind(('', PORT)) 
	print 'Listening for broadcast at', s.getsockname() 
	while True:
		data, address = s.recvfrom(MAX) 
		print 'The client at %r says : %r' %(address,data) 

elif sys.argv[1] == 'client':
	network= sys.argv[2] 
	s.sendto('Broadcast Message!',(network,PORT)) #the message is sent out to multiple servers connected on the same network, that is why we mention a network address and not a particular IP

else:
	print >>sys.stderr, 'usage: filename.py server'
	print >>sys.stderr, 'usage: filename.py client <host>'
	sys.exit(2) 

