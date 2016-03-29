import json
data = '''[
{
	"name":"Shreyas",
	"phone":
	{
	"type": "intl",
	"number": "+1 469 999 3800"
	},

	"email" : 
	{
	"hide" : "yes",
	"addr" : "shreyas.enug@gmail.com"
	}
},
{
	"name":"Gune",
	"phone":
	{
	"type": "intl",
	"number": "+1 467 999 3800"
	},

	"email" : 
	{
	"hide" : "yes",
	"addr" : "gune.enug@gmail.com"
	}
}]

'''
info  = json.loads(data)
# print 'Hide:',info["email"]["hide"]
# print 'Name:',info["name"]
# print 'Email:',info["email"]["addr"]
# print  'Phone:',info["phone"]["number"]

print 'user count:', len(info),'\n'
for item in info:
	print 'Name:', item['name']
	print 'Number:',item['phone']['number']
	print 'Email:', item['email']['addr']
	print '\n'
