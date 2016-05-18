#!/usr/bin/env python
import sys

#exit statement
if len(sys.argv)!=2:
	#exit
	print sys.exit("Usage: ./ip2bin.py <ip_address>")

#get the IP from the argument list
ip_addr = sys.argv.pop()

#get the octets out of the argument list
octets = ip_addr.split(".") 

#create a blank list to store the binary converted values
ip_addr_bin = [] 

#check if length of the Octets is 4 
if len(octets) == 4 :
	#loop through the octet list
	for octet in octets:
		#store the binary version of the INT in a variable called bin_octet
		bin_octet = bin(int(octet)) 
		
		#get rid of the 0b from the front of string. 
		bin_octet = bin_octet[2:] #so, this basically cuts of the first two characters
		
		#pad it so that everything is 8 characters long
		while True:
			if len(bin_octet) >= 8:
				break
			bin_octet = '0' + bin_octet
		#put all of this back in the ip_addr_bin[] list 
		ip_addr_bin.append(bin_octet) 
	#join everything
	ip_addr_bin = ".".join(ip_addr_bin) 
	
	#print the outputs
	print "\n %-15s %-45s" %("IP Address ", "Binary") 
	print "%-15s %-45s\n\n"%(ip_addr,ip_addr_bin) 
else:
	sys.exit("Invalid IP entered") 




