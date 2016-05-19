#!/usr/bin/env python

'''This program basically deals with Cisco's 'show version' command. If you don't know 
how it looks, it looks like this : 

Note : This is going to be a long text. 

device# show version
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
ROM: System Bootstrap, Version 12.4(22r)YB5, RELEASE SOFTWARE (fc1)
twb-sf-881 uptime is 7 weeks, 5 days, 19 hours, 23 minutes
System returned to ROM by reload at 15:33:36 PST Fri Feb 28 2014
System restarted at 15:34:09 PST Fri Feb 28 2014
System image file is "flash:c880data-universalk9-mz.150-1.M4.bin"
Last reload type: Normal Reload
Last reload reason: Reload Command
Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX1000038X
5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)
License Info:
License UDI:
-------------------------------------------------
Device#   PID                   SN
-------------------------------------------------
*0        CISCO881-SEC-K9       FTX1000038X
License Information for 'c880-data'
    License Level: advipservices   Type: Permanent
    Next reboot license Level: advipservices
Configuration register is 0x2102

What this program does is gets some useful data out of this whole thing. Data such as :
(vendor, model, os_version, uptime and serial_number).  And It's going to work for all devices.

'''

import pprint

#let us store the whole of 'show version' dump. In an active case, you'll get this from a SSH connected request for show version.

show_version = '''
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
ROM: System Bootstrap, Version 12.4(22r)YB5, RELEASE SOFTWARE (fc1)
twb-sf-881 uptime is 7 weeks, 5 days, 19 hours, 23 minutes
System returned to ROM by reload at 15:33:36 PST Fri Feb 28 2014
System restarted at 15:34:09 PST Fri Feb 28 2014
System image file is "flash:c880data-universalk9-mz.150-1.M4.bin"
Last reload type: Normal Reload
Last reload reason: Reload Command
Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX1000038X
5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)
License Info:
License UDI:
-------------------------------------------------
Device#   PID                   SN
-------------------------------------------------
*0        CISCO881-SEC-K9       FTX1000038X
License Information for 'c880-data'
    License Level: advipservices   Type: Permanent
    Next reboot license Level: advipservices
Configuration register is 0x2102
'''

#get this massive data chunk as a list, by lines.
show_ver_list = show_version.split("\n") 

#I am going to store the useful info in a dictionary.
router_info = {} #this is an empty dictionary

#lets iterate through our list and get some meaningful stuff out.

for i in show_ver_list:
	#let the checking begin
	if 'Cisco IOS Software' in i:
		router_info['vendor'] = 'Cisco' #this could be Juniper/Ericsson
		#now, take the line that you have, and split it by ','.
		os_version = i.split(',')[2] #this pulls out the version, at [2] on line1
		router_info['os_version'] = os_version
 
	if 'System Bootstrap' in i:
		rom_version=i.split('Version ')[1]
		rom_v = rom_version.split(",")[0] 
		router_info['ROM_version']= rom_v

	if 'bytes of memory' in i:
		router_info['model']= i.split()[1]

	if 'Processor board ID' in i:
		router_info['serial_number'] = i.split()[3]
	
	if ' uptime is ' in i:
		uptime = i.split(' uptime is ')[1]  
		uptime = uptime.strip() #takes out all the whitespaces
		router_info['uptime'] = uptime 

print
pprint.pprint(router_info) 

print 

