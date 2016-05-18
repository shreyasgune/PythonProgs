#!/usr/bin/env python

'''
A.Check for 4 octets in IP
B. The first Octet should be 1-223
C. First Octet cannot be 127 , this is loopback
D. The IP cannot be : 169.254.X.X .
E. The last three octets should be from 0-255 

''' 

import sys

if len(sys.argv) != 2:
	sys.exit("Usage : ./ip_verify.py <ip_address>") 
	
ip_addr = sys.argv.pop() 

valid_ip = True 

#split the IP address according to the "." 
octets = ip_addr.split(".") 

#check if this is greater than 4 values 
if len(octets) != 4 :
	sys.exit("\n INVALID IP %s " %ip_addr) 

#convert octet from string to int 
for i,octet in enumerate(octets) :
	#handle some exceptions
	try:
		octets[i] = int(octet) 
	except ValueError:
		#conversion not possible
		sys.exit("\n Invalid IP") 

first,second,third,fourth = octets 
print first, second, third, fourth 

#check the conditions
if first<1 or first>223 or first == 127 :
	valid_ip = False

#check the 169.254.X.X condition
if first == 169 and second == 254:
	valid_ip = False

#check the last three octet rule
for octet in (second,third,fourth):
	if(octet<0)or(octet>255):
		valid_ip = False 

if valid_ip:
	print "The IP address %s is valid." %ip_addr 
else:
	sys.exit("\n INVALID IP") 


