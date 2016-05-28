#!/usr/bin/env python
#Trying to send a big UDP Packet to a server

import IN, socket, sys
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#AF_INET = address family of IPv4 , SOCK_STREAM = connection oriented TCP so , SOCK_DGRAM = UDP

'''
A pair (host, port) is used for the AF_INET address family, where host is a string representing either a hostname in Internet domain notation like 'daring.cwi.nl' or an IPv4 address like '100.50.200.5', and port is an integer. '''




MAX = 65535
PORT = 1060

hostname = sys.argv[1] #cuz the [0] is going to be a blank
s.connect((hostname,PORT))
s.setsockopt(socket.IPPROTO_IP, IN.IP_MTU_DISCOVER, IN.IP_PMTUDISC_DO)
'''
This is just a explaination of why use : MTU stuff for sockopt 
import socket
IP_MTU_DISCOVER   = 10
IP_PMTUDISC_DONT  =  0  # Never send DF frames.
IP_PMTUDISC_WANT  =  1  # Use per route hints.
IP_PMTUDISC_DO    =  2  # Always DF.
IP_PMTUDISC_PROBE =  3  # Ignore dst pmtu.
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("10.0.0.1", 8000))
s.send("Hello World!") # DF bit is set in this packet
s.setsockopt(socket.SOL_IP, IP_MTU_DISCOVER, IP_PMTUDISC_DONT)
s.send("Hello World!") # DF bit is cleared in this packet
'''

try:
	s.send("#"*65000)
	

'''
 exception socket.error

This exception is raised for socket-related errors. The accompanying value is either a string telling what went wrong or a pair (errno, string) representing an error returned by a system call, similar to the value accompanying os.error. See the module errno, which contains names for the error codes defined by the underlying operating system.
'''

except socket.error:
	print 'The message did not make it'
	option = getattr(IN,'IP_MTU',14) # this is taken from linux/in.h 
	print 'MTU:', s.getsockopt(socket.IPPROTO_IP,option) 

else:
	print 'The big message was sent! This is cool cuz your network supports big packets.'

'''
Additional Notes

value = s.getsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, value)

Many options are specific to particular operating systems, and may be finicky about how their options are presented. Here are some of the more common:

• SO_BROADCAST: Allows broadcast UDP packets to be sent and received; see the next
section for details.

• SO_DONTROUTE: Only be willing to send packets that are addressed to hosts on
subnets to which this computer is connected directly. My laptop, for example, at
this moment would be willing to send packets to the networks 127.0.0.0/8 and
192.168.5.0/24 if this socket option were set, but would not be willing to send
them anywhere else.

• SO_TYPE: When passed to getsockopt(), this returns to you regardless of whether a
socket is of type SOCK_DGRAM and can be used for UDP, or it is of type SOCK_STREAM
and instead supports the semantics of TCP.
'''

