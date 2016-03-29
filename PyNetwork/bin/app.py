import web
import urllib
import json


urls = ("/","Index","/geolocate","Index"
        
                    )
app = web.application(urls, globals())

# render = web.template.render('templates/')
render = web.template.render('c:/opppo/pynetwork/webapp/templates/')
class Index(object):
    def GET(self):
        return render.geo_form()

    def POST(self):
    	serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
    	form = web.input(addr = " ")
    	address = form.addr
    	url = serviceurl+urllib.urlencode({'sensor':'false','address': address})
    	uh = urllib.urlopen(url)
    	data = uh.read()
    	js = json.loads(str(data))
    	lat = js["results"][0]["geometry"]["location"]["lat"]
    	lng = js["results"][0]["geometry"]["location"]["lng"]
    	location = js['results'][0]['formatted_address']
        latlon = str(lat)+','+str(lng) 
        img_url1 = 'http://maps.googleapis.com/maps/api/staticmap?maptype=satellite&center='+latlon+'&zoom=18&size=400x300&sensor=false'
        img_url2 = 'http://maps.googleapis.com/maps/api/staticmap?center='+latlon+'&zoom=18&size=400x300&sensor=false'
    	return render.geolocate(adde = address,lat =lat,lng =lng,loca=location,urlz =img_url1,urlzz=img_url2)

if __name__ == "__main__":
	app.run()

# import web

# urls = ( '/','index')

# class index:
#     def GET(self):
#         return "Hello World"

# if __name__ == "__main__":
#     app = web.application(urls,globals())
#     app.run()