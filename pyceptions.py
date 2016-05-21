#!/usr/bin/env python

a= {}
b= [] 
a['name'] = 'whateer'  
print 'Hello'

try:
	print 'string2'
	print a['name']
	print b[3]  
	print 'string3'
except KeyError as e :
	print 'There was a key exception'
except IndexError as e:
	print str(e) 
	print 'There was an index exception'	
print 'world' 


