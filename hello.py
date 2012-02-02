import cherrypy

class HelloWorld:
    def index(self):
        return "Hello CherryPy!"
    index.exposed = True
cherrypy.quickstart(HelloWorld())