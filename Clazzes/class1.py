#Suppose we do this
'''
def create_network_device(ip, username, password):
	net_dev={}
	net_dev['ip'] = ip
	net_dev['username'] = username
	net_dev['password'] = password
	return net_dev

rtr1 = create_network_device('1.2.3.4','gune','pass') 
rtr2 = create_network_device('192.168.3.2','shreyas','pass2') 


print rtr1
print rtr2 
'''

#same thing as above but , using Classes
'''
class NetworkDevice(object):
	pass

rtr3 = NetworkDevice() 


rtr3.ip = '1.1.1.10' 
rtr3.username = 'gune' 
rtr3.password = 'pass'

print rtr3

''' 

#using classes the right way
class NetworkDevice(object):
	def __init__(self,ip,username,password):
		self.username = username
		self.ip = ip
		self.password = password
		 
rtr = NetworkDevice('10.3.4.1','gune','some') 

print rtr 
print rtr.ip,' ',rtr.username,' ',rtr.password

#differentiation between attributes, parameters and arguments
class NetworkDevice2(object):
	def __init__(self,ip,username,password):
		self.x = ip
		self.y = username
		self.z = password 
rtr2 = NetworkDevice2('19.2.3.4','shreyas','passzwrd') 
print rtr2.x,' ',rtr2.y,' ',rtr2.z 

class SomeClass(object):
	def __init__(self,x,y): #x and y here are parameters
		self.x = x
		self.y = y

	def a_sum(self):
		return self.x + self.y
	def a_product(self):
		return self.x*self.y

a = SomeClass(3,4)  # 3 and 4 are arguments 
print a.x, a.y    #x and y are attributes, so basically, attributes are only created when an object is created, so the parameters defined for the class become attributes of the object created 
print 'Sum',a.a_sum()
print 'Product',a.a_product() 


#have fun with some strings
'''
str = '1.2.4.5'
print str.split(".") 
'''

print 'some inheritance'

class NewClass(SomeClass):
	pass

b = NewClass(4,5) 
print b.x , b.y
print 'sum' , b.a_sum() 
print 'product',b.a_product() 


print 'some newest class inheritance with different init parameters'
class NewestClass(SomeClass):
	def __init__(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z
		#this init overwrites the parent class init
		#to call the init from parent class
		SomeClass.__init__(self,x,y) 

z = NewestClass(8,9,10)
print z.x,z.y,z.z 

print 'sum',z.a_sum()
print 'product',z.a_product() 





