"""
import web

urls = (
  '/', 'index'
)

app = web.application(urls, globals())

class index:
    def GET(self):
        #greeting = "Hello World"
        return greeting

if __name__ == "__main__":
    app.run()
""" 
import web

urls = (
  '/hello', 'Index'
)

app = web.application(urls, globals())

#render = web.template.render('templates/')
render = web.template.render('templates/', base="layout")
class Index(object):
    
    def GET(self):
        return render.hello_form()
    
    def POST(self):
        form = web.input(name="Nobody",greet="Hello")
        greeting = "%s,%s" % (form.greet,form.name)
        return render.index(greeting = greeting)
        """
        form = web.input(name="Nobody",greet=None)
        if form.greet:
            greeting = "Hello ,%s %s" % (form.name,form.greet)
            return render.index(greeting = greeting)
        else:
            return "ERROR:greet is required"
       """
if __name__ == "__main__":
    app.run()