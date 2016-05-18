#!/usr/bin/python

# Frm a given 'show ip int br' , I'm going to create a list where each element in the list
# is a tuple consisting of (interface_name,ip_address,status,protocol). Only include interfaces that# are up and running

import pprint 
#used to print a list

# right now I am hard coding it but this would be populated with stuff that is pulled from an SSH
# session into a router or a switch.
show_ip_int_brief = '''
Interface      IP-Address     OK?     Method     Status     Protocol
FastEthernet0  unassigned     YES      unset       up          up
FastEthernet1  unassigned     YES      unset       up          up 
FastEthernet3  unassigned     YES      unset      down        down
FastEthernet4   6.9.4.10      YES      unset       up         down
NVI0            6.9.4.10      YES      NVRAM       up         down
'''

#break the long string into list based on new lines
show_ip_lines = show_ip_int_brief.split("\n") 

#make a new blank list to append into
show_ip_list = [] 

for line in show_ip_lines:
	#skip the header line
	if 'Interface' in line:
		continue
	
	#break the lines into words
	line_split = line.split() 

	#filter out lines that don't have the correct number of fields
	if len(line_split) == 6:
		#map the variables to the fields in the line_split list (this is so fun)
		if_name, ip_addr, discard1,discard2 , line_status, line_proto = line_split
	
		if (line_status=="up") and (line_proto=="up"):
			show_ip_list.append((if_name,ip_addr,line_status,line_proto))

print "\n"

pprint.pprint(show_ip_list)
print "\n"


 
