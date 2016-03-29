# import xml.etree.ElementTree as ET 

# data = ''' 
# <person>
# 	<name> Shreyas </name>
# 	<phone type="intl">+1 469 999 3800</phone>
# 	<email hide = "yes" />
# </person> ''' 

# tree = ET.fromstring(data)
# print 'Name:', tree.find('name').text 
# print 'Attr:', tree.find('email').get('hide')
# print 'Phone:', tree.find('phone').text 
# input = ''' <stuff>
# <users>
# <user x="2">
# <id>001</id>
# <name>Shreyas</name>
# </user>
# <user x="7">
# <id>009</id>
# <name>Gune</name>
# </user>
# </users>
# </stuff>'''
# stuff = ET.fromstring(input)
# lst = stuff.findall('users/user')
# print 'User count:',len(lst)
# for item in lst:
# 	print 'Name:',item.find('name').text
# 	print 'ID:',item.find('id').text
# 	print 'Attribute:',item.get("x")
