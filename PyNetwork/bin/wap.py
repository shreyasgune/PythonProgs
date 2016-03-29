import web

urls = (
  '/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('c:/opppo/pyNetwork/webapp/templates/')

class Index(object):
    def GET(self):
        return render.storm()

    def POST(self):
        form = web.input(name="Nobody", greet="Hello")
        greeting = "%s, %s" % (form.greet, form.name)
        return render.flex(greeting = greeting)

if __name__ == "__main__":
    app.run()