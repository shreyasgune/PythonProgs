class NetworkDevice(object):
	def __init__(self,ip,username,password):
		self.ip = ip
		self.username = username
		self.password = password 

	def connect_to_device(self):
		#SSH or telnet

	def enter_enable_mode(self):
		#conf t

	def show_version(self):
		#get data to make more commands
	
